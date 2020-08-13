import argparse


def parse():
    parser = argparse.ArgumentParser(
        description="Sort pictures directly on your computer!"
    )

    parser.add_argument("Path", help="Path of the folder you want to sort")
    args = parser.parse_args()

    return args
