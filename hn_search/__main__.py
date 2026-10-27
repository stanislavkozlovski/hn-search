"""Collect research metadata, archive discussions, or run the Telegram feed."""

import argparse
from contextlib import closing
import sys
import time
from urllib.request import urlopen

from hn_search.catalog import open_catalog
from hn_search.collect import collect_daily, collect_history


def main(argv=None, *, opener=urlopen, clock=time.time):
    parser = argparse.ArgumentParser(description="Collect Hacker News metadata, archive discussions, or send a Telegram feed")
    parser.add_argument("--db", help="SQLite database path (archive default: hn.sqlite3)")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("collect")
    archive_parser = commands.add_parser("archive")
    archive_parser.add_argument("ids", nargs="+", type=int, help="Catalog story IDs")
    archive_parser.add_argument("--export-dir", default="exports", help="Export directory (default: exports)")
    feed = commands.add_parser("feed")
    feed.add_argument("--config", required=True, help="TOML lens configuration")
    args = parser.parse_args(argv)
    if args.command != "archive" and args.db is None:
        parser.error(f"{args.command} requires --db")
    if args.command == "feed":
        from hn_search.feed.run import feed_command

        return feed_command(args.db, args.config, opener=opener, clock=clock)
    if args.command == "archive":
        from hn_search.archive import UncataloguedStories, archive

        try:
            with closing(open_catalog(args.db or "hn.sqlite3")) as conn:
                archive(conn, args.ids, args.export_dir, opener=opener, clock=clock)
        except UncataloguedStories as error:
            for root in error.roots:
                print(f"error: {root} is not in the catalog; archive accepts only catalog stories", file=sys.stderr)
            return 1
        except Exception as error:
            print(f"error: {error}", file=sys.stderr)
            for note in getattr(error, "__notes__", ()):
                print(note, file=sys.stderr)
            return 1
        return 0
    with closing(open_catalog(args.db)) as conn:
        collect_history(conn, opener=opener)
        collect_daily(conn, opener=opener, clock=clock)


if __name__ == "__main__":
    raise SystemExit(main())
