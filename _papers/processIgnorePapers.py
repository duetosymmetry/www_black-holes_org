#!/usr/bin/env python

import argparse
import subprocess
from warnings import warn

############################################################

if __name__ == "__main__":
    help = """Remove one or more bibkeys' markdown files, and add it (them) to
    the list of papers to ignore."""
    parser = argparse.ArgumentParser(
        description=help, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--ignore-file",
        type=argparse.FileType('r+'),
        default="papersToIgnore.txt",
        required=False,
        help="""Path to a file with bibkeys to ignore, one bibkey per line.
(default: %(default)s)"""
    )
    parser.add_argument(
        "bibkeys",
        nargs='+',
        help="""INSPIRE bibkey(s) of papers to remove from repo and add to the
        ignore-file."""
    )

    args = parser.parse_args()

    ignore_bibs = [line.strip() for line in args.ignore_file.readlines()]

    bibkeys = set(args.bibkeys)

    for bibkey in bibkeys:
        if bibkey in ignore_bibs:
            warn(f"bibkey {bibkey} alread in {args.ignore_file}. Bailing out.")
            raise ValueError(bibkey)

    for bibkey in bibkeys:
        git_rm_result = subprocess.run(['git', 'rm', bibkey + '.md'],
                                       check=True)
        args.ignore_file.write(bibkey + '\n')

    args.ignore_file.flush()
    args.ignore_file.close()

    git_add_result = subprocess.run(['git', 'add', args.ignore_file.name],
                                    check=True)
