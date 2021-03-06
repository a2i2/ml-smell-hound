import argparse

from main import Runner


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()

    my_parser.add_argument(
        "dir_path", metavar="dir_path", type=str, help="the directory to process"
    )

    my_parser.add_argument(
        "metamodel",
        metavar="metamodel",
        type=str,
        choices=["ml", "non_ml", "context"],
        help="ml, non_ml or context",
    )

    args = my_parser.parse_args()
    print(vars(args))
    runner = Runner(args.dir_path, args.metamodel)
    runner.exec()
