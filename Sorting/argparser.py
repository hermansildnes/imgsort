import argparse


def parse():
    parser = argparse.ArgumentParser(
        description="Sort pictures directly on your computer!"
    )

    parser.add_argument("Path")

    return parser.parse_args()
