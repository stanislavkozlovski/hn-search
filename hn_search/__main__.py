"""Collect research metadata or run the independent Telegram feed."""

import argparse
from contextlib import closing
import time
from urllib.request import urlopen

from hn_search.catalog import open_catalog
from hn_search.collect import collect_daily, collect_history


def main(argv=None, *, opener=urlopen, clock=time.time):
    parser = argparse.ArgumentParser(description="Collect Hacker News metadata or send a Telegram feed")
    parser.add_argument("--db", required=True, help="SQLite database path for the selected command")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("collect")
    feed = commands.add_parser("feed")
    feed.add_argument("--config", required=True, help="TOML lens configuration")
    args = parser.parse_args(argv)
    if args.command == "feed":
        from hn_search.feed.run import feed_command

        return feed_command(args.db, args.config, opener=opener, clock=clock)
    with closing(open_catalog(args.db)) as conn:
        collect_history(conn, opener=opener)
        collect_daily(conn, opener=opener, clock=clock)


if __name__ == "__main__":
    main()
