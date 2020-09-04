import argparse


def parse():
    parser = argparse.ArgumentParser(
        description="Sort pictures directly on your computer!"
    )

    parser.add_argument(
        "-p",
        "--path",
        help="Full path of the folder you want to sort. Default=current",
    )
    args = parser.parse_args()

    return args
