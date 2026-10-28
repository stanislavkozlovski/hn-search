"""The sequential search → archive → classify → analyze → report workflow."""

import importlib.metadata
import io
import shutil
import sys
import tempfile
import time
from collections import Counter
from contextlib import closing, redirect_stdout
from http.client import HTTPException
from pathlib import Path

from hn_search.archive import archive_story as download_story
from hn_search.archive_export import _snapshot
from hn_search.catalog import open_catalog

from . import store
from .ai import cited_ids, input_limit, resolve_codex_runtime, run_stage
from .conversation import agree_keywords, agree_settings
from .progress import Progress
from .prompts import PROMPTS, story_call, story_instructions
from .render import analysis_md, comment_refs, report_md, thread_md
from .search import gate_lines, search
from .threads import combine_verdicts, estimate_tokens, load_export, pack, split_story


def _setting(name, settings):
    return settings["classification" if name in ("description", "verdict") else "thread_analysis"]


def _plans(snapshot, name, settings, question):
    setting = _setting(name, settings)
    question = "" if name == "description" else question
    room = input_limit(setting["model"]) - estimate_tokens(story_instructions(name, question))
    return split_story(snapshot, room)


def _key(unit, name, settings, question):
    setting = _setting(name, settings)
    return store.ResultKey(name, unit.story_id, unit.part, PROMPTS[name].version, setting["model"],
                           setting["effort"], unit.input_key, "" if name == "description" else question)


def _reused_stories(conn, matches, settings, question):
    reused = []
    for story_id in matches.posts:
        row = conn.execute("SELECT status FROM archives WHERE root_id = ?", (story_id,)).fetchone()
        if row is None or row[0] != "complete":
            continue
        snapshot = _snapshot(conn, story_id)
        if snapshot["root"]["item"] is not None and all(
            store.lookup(conn, _key(unit, name, settings, question)) is not None
            for name in ("description", "verdict")
            for unit in _plans(snapshot, name, settings, question)
        ):
            reused.append(story_id)
    return reused


def _story_stage(conn, run_id, snapshots, name, settings, question, client, cwd, progress, clock):
    plans = {sid: _plans(snapshot, name, settings, question) for sid, snapshot in snapshots.items()}
    units = [unit for story in plans.values() for unit in story]
    keys = {(unit.story_id, unit.part): _key(unit, name, settings, question) for unit in units}
    results = {identity: saved for identity, key in keys.items() if (saved := store.lookup(conn, key)) is not None}
    missing = [unit for unit in units if (unit.story_id, unit.part) not in results]
    setting = _setting(name, settings)
    call_question = "" if name == "description" else question
    room = input_limit(setting["model"]) - estimate_tokens(story_instructions(name, call_question))
    calls = [[unit] for unit in missing] if name == "analysis" else pack(missing, room)
    stage = "analyze" if name == "analysis" else "classify"
    completed = set()

    def complete_rows(available, story_ids):
        rows = []
        for sid in sorted(story_ids):
            if all((sid, unit.part) in available for unit in plans[sid]):
                if name == "verdict":
                    verdict = combine_verdicts([available[(sid, unit.part)].result for unit in plans[sid]])
                    rows.append((sid, verdict["verdict"], verdict["reasons"]))
        return rows

    for sid, status, reason in complete_rows(results, plans):
        store.set_status(conn, run_id, sid, status, reason)

    def show_completed():
        for sid in plans:
            if sid not in completed and all((sid, unit.part) in results for unit in plans[sid]):
                completed.add(sid)
                reused = all((unit.story_id, unit.part) not in missing_ids for unit in plans[sid])
                if name == "verdict":
                    verdict = combine_verdicts([results[(sid, unit.part)].result for unit in plans[sid]])
                    progress.event(f"{verdict['verdict']} {sid} {snapshots[sid]['root']['item'].get('title', '')}"
                                   + (" · reused" if reused else ""))
                else:
                    progress.event(f"{name} {sid} " + ("reused" if reused else "complete"))
        summary = f"{len(completed)}/{len(plans)}"
        if name == "verdict":
            tallies = Counter(combine_verdicts([results[(sid, unit.part)].result for unit in plans[sid]])["verdict"]
                              for sid in completed)
            summary += " · " + " · ".join(f"{tallies[value]} {value}" for value in ("relevant", "uncertain", "irrelevant"))
        progress.update(stage, summary if name != "description" else "descriptions " + summary)

    missing_ids = {(unit.story_id, unit.part) for unit in missing}
    show_completed()
    for index, call in enumerate(calls, 1):
        label = f"{name} call {index}/{len(calls)} · {len(call)} units · {setting['model']} {setting['effort']}"
        allowed = {sid: set(comment_refs(snapshot)) for sid, snapshot in snapshots.items()}
        with progress.busy(stage, label):
            reply = run_stage(client, name, story_call(name, call_question, call), cwd=cwd,
                              model=setting["model"], effort=setting["effort"], units=call,
                              allowed_ids=allowed[call[0].story_id] if name == "analysis" else allowed,
                              call_label=f"{name} call {index}/{len(calls)}")
        output = {(item["story_id"], item["part"]): item for item in reply.output["stories"]} if name != "analysis" else {
            (call[0].story_id, call[0].part): reply.output}
        pending = {identity: store.SavedResult(0, keys[identity], result) for identity, result in output.items()}
        statuses = complete_rows(results | pending, {unit.story_id for unit in call})
        rows = []
        for identity, result in output.items():
            citations = cited_ids(result) | set(result.get("comment_ids", []))
            rows.append((keys[identity], result, citations))
        for saved in store.save_call(conn, run_id, rows, reply.usage, now=clock(), statuses=statuses):
            results[(saved.key.story_id, saved.key.part)] = saved
        show_completed()
    return {sid: [results[(sid, unit.part)] for unit in units] for sid, units in plans.items()}


def _synthesis_prompt(question, stories):
    index = [{"story_id": story["snapshot"]["root_id"],
              "path": f"stories/{story['snapshot']['root_id']}/analysis.md",
              "title": story["snapshot"]["root"]["item"].get("title", ""),
              "descriptions": story["descriptions"]} for story in stories]
    inline = PROMPTS["synthesis"].render(question=question, thread_index=index,
                                          analyses=[{"story_id": story["snapshot"]["root_id"],
                                                     "parts": story["analyses"]} for story in stories])
    return inline, index


def _synthesize(conn, run_id, question, settings, stories, client, cwd, folder, progress, clock):
    if not stories:
        return None
    inline, index = _synthesis_prompt(question, stories)
    setting = settings["report"]
    name = "synthesis" if estimate_tokens(inline) <= input_limit(setting["model"]) else "folder_synthesis"
    prompt = inline if name == "synthesis" else PROMPTS[name].render(question=question, thread_index=index)
    row_ids = sorted({row_id for story in stories for row_id in story["row_ids"]})
    key = store.ResultKey("synthesis", 0, 0, PROMPTS[name].version, setting["model"], setting["effort"],
                          "rows:" + ",".join(map(str, row_ids)), question)
    cached = store.lookup(conn, key)
    if cached is not None:
        progress.event("synthesis reused")
        return cached.result
    allowed = {cid for story in stories for cid in comment_refs(story["snapshot"])}
    with progress.busy("report", f"{name} · {setting['model']} {setting['effort']}"):
        result = run_stage(client, name, prompt, cwd=folder if name == "folder_synthesis" else cwd,
                           model=setting["model"], effort=setting["effort"], allowed_ids=allowed,
                           source_story_ids=[story["snapshot"]["root_id"] for story in stories])
    store.save_call(conn, run_id, [(key, result.output, cited_ids(result.output))], result.usage, now=clock())
    progress.event(name + " complete")
    return result.output


def run_research(conn, out_dir, *, client, archive_story, ask, stream, clock):
    if store.next_folder(conn, out_dir).exists():
        raise FileExistsError(f"research run folder already exists: {store.next_folder(conn, out_dir)}")
    progress = Progress(stream, clock)
    try:
        with tempfile.TemporaryDirectory(prefix="hn-research-") as temporary:
            scratch = Path(temporary)
            cwd, exports = scratch / "cwd", scratch / "exports"
            cwd.mkdir()
            settings = agree_settings(client, cwd, ask, progress)
            progress.event("Question?")
            question = progress.ask(ask)
            if not question.strip():
                raise ValueError("research question cannot be empty")
            approved = agree_keywords(client, cwd, settings, ask, progress, question=question)
            while True:
                with progress.busy("search", "searching the local catalog"):
                    matches = search(conn, approved.keywords)
                    reused = _reused_stories(conn, matches, settings, approved.question)
                    room = input_limit(settings["classification"]["model"]) - estimate_tokens(
                        story_instructions("verdict", approved.question))
                    lines = gate_lines(matches, room=room, reused=reused)
                progress.event("\n".join(lines))
                reply = progress.ask(ask)
                revised = agree_keywords(client, cwd, settings, ask, progress, state=approved,
                                         first_reply=reply, gate=lines)
                if revised.question == approved.question and revised.keywords == approved.keywords:
                    break
                approved = revised
            question = approved.question
            run_id, folder = store.create_run(conn, out_dir, question, approved.keywords, settings,
                                              matches.posts, now=clock())
            progress.checklist = True
            progress.update("search", f"{len(matches.posts)} stories", done=True)
            snapshots = {}
            for index, story_id in enumerate(matches.posts, 1):
                output = io.StringIO()
                try:
                    with progress.busy("download", f"story {story_id}"):
                        with redirect_stdout(output):
                            archive_story(conn, story_id, exports)
                        snapshot = load_export(exports / f"{story_id}.json")
                except (OSError, ValueError, HTTPException) as error:
                    store.set_status(conn, run_id, story_id, "not_downloaded", str(error))
                    progress.event(f"not downloaded {story_id}: {error}")
                else:
                    for line in output.getvalue().splitlines():
                        progress.event(line)
                    if snapshot["root"]["item"] is None:
                        store.set_status(conn, run_id, story_id, "unavailable", "HN returned a null root")
                        progress.event(f"unavailable {story_id}: HN returned a null root")
                    else:
                        snapshots[story_id] = snapshot
                        progress.event(f"download {story_id} complete")
                progress.update("download", f"{index}/{len(matches.posts)}")
            progress.update("download", f"{len(matches.posts)}/{len(matches.posts)}", done=True)
            descriptions = _story_stage(conn, run_id, snapshots, "description", settings, question,
                                        client, cwd, progress, clock)
            verdicts = _story_stage(conn, run_id, snapshots, "verdict", settings, question,
                                    client, cwd, progress, clock)
            progress.update("classify", progress.summaries["classify"], done=True)
            relevant = {sid: snapshot for sid, snapshot in snapshots.items()
                        if combine_verdicts([row.result for row in verdicts[sid]])["verdict"] == "relevant"}
            for story_id, snapshot in relevant.items():
                story_folder = folder / "stories" / str(story_id)
                story_folder.mkdir(parents=True)
                shutil.copyfile(exports / f"{story_id}.json", story_folder / "thread.json")
                (story_folder / "thread.md").write_text(thread_md(snapshot))
            analyses = _story_stage(conn, run_id, relevant, "analysis", settings, question,
                                    client, cwd, progress, clock)
            progress.update("analyze", f"{len(relevant)}/{len(relevant)}", done=True)
            stories = []
            for story_id, snapshot in relevant.items():
                description_parts = [row.result for row in descriptions[story_id]]
                analysis_parts = [row.result for row in analyses[story_id]]
                verdict = combine_verdicts([row.result for row in verdicts[story_id]])
                (folder / "stories" / str(story_id) / "analysis.md").write_text(
                    analysis_md(snapshot, description_parts, verdict, analysis_parts))
                rows = descriptions[story_id] + verdicts[story_id] + analyses[story_id]
                stories.append({"snapshot": snapshot, "descriptions": description_parts,
                                "analyses": analysis_parts, "row_ids": [row.id for row in rows]})
            synthesis = _synthesize(conn, run_id, question, settings, stories, client, cwd, folder, progress, clock)
            report = folder / "report.md"
            report.write_text(report_md(question, approved.keywords, settings, stories, synthesis,
                                        store.coverage(conn, run_id)))
            store.finish_run(conn, run_id, now=clock())
            progress.update("report", "complete", done=True)
            progress.close()
            progress.event(f"report {report}")
            return report
    finally:
        progress.close()


def main(db="hn.sqlite3", out="research"):
    def usage_error(message):
        print("error: " + message, file=sys.stderr)
        raise SystemExit(2)

    if not Path(db).is_file():
        usage_error(f"no catalog at {db}; run collect first or pass --db")
    try:
        version = importlib.metadata.version("stan-ai-client")
    except importlib.metadata.PackageNotFoundError:
        usage_error("research requires stan-ai-client==0.1.19")
    if version != "0.1.19":
        usage_error(f"research requires stan-ai-client==0.1.19; installed {version}")
    with closing(open_catalog(db)) as conn:
        store.migrate(conn)
        if store.next_folder(conn, out).exists():
            usage_error(f"research run folder already exists: {store.next_folder(conn, out)}")
        from stan_ai_client import CodexClient
        try:
            executable = resolve_codex_runtime()
        except (OSError, ValueError) as error:
            usage_error(str(error))
        run_research(conn, out, client=CodexClient(executable=str(executable)), archive_story=download_story,
                     ask=input, stream=sys.stdout, clock=time.time)
    return 0
