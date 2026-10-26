"""Run with python3 -m hn_search --db PATH collect."""

import argparse
from contextlib import closing
import time
from urllib.request import urlopen

from hn_search.catalog import open_catalog
from hn_search.collect import collect_daily, collect_history


def main(argv=None, *, opener=urlopen, clock=time.time):
    parser = argparse.ArgumentParser(description="Collect Hacker News post metadata")
    parser.add_argument("--db", required=True, help="SQLite catalog path")
    parser.add_subparsers(dest="command", required=True).add_parser("collect")
    args = parser.parse_args(argv)
    with closing(open_catalog(args.db)) as conn:
        collect_history(conn, opener=opener)
        collect_daily(conn, opener=opener, clock=clock)


if __name__ == "__main__":
    main()
