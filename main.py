import argparse
import os
from solve import solve_engine
from setup import setup_engine


def arg_parser():
    parser = argparse.ArgumentParser(description="DSA CLI App")
    parser.add_argument("--setup", metavar="", help="setup an environment")
    parser.add_argument("--solve", metavar="", help="solve a question")
    return parser


def main():
    parser = arg_parser()
    args = parser.parse_args()
    if args.setup:
        setup_engine(args.setup)
    elif args.solve:
        solve_engine(args.solve)
    else:
        parser.print_help()


if __name__ == '__main__':
    print("hello world")
    main()
