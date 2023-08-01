"""Something something

Usage:
    verify (-d PATH) [-qv]

Options:
    -d, --dir DIR       Path to the blockchain
    -v, --verbose       Verbose output [default: False]
    -q, --quiet         Quiet output [default: False]

"""

import os
import sys

from docopt import docopt


def add(a, b):
    return a + b


def div(a, b):
    return a / b


def main(folder: str, verbosity=False, quiet=False) -> int:
    """Do something
    @param folder: The folder to verify the blockchain in.
    @param verbosity: Whether to print verbose output.
    @param quiet: Whether to print quiet output.
    @return: An integer indicating whether the command is successful
             0 for success, 1 for failure. This makes it easy to compose
             this command in a bash script.

    """
    if verbosity and not quiet:
        print(f"🔎 {folder}")

    ok = (True,)

    return 0 if ok else 1


if __name__ == "__main__":
    arguments = docopt(__doc__, version="something 0.1")
    folder = os.path.join(os.getcwd(), arguments["--dir"])
    v, q = arguments["--verbose"], arguments["--quiet"]
    sys.exit(main(folder, v, q))
