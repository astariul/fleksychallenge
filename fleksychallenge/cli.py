import argparse

from fleksychallenge import interact, prepare, train


def cli():
    parser = argparse.ArgumentParser(description="Fleksy challenge part 1")
    parser.add_argument("cmd", help="Command to execute", choices=["prepare", "train", "interact"])
    args = parser.parse_args()

    if args.cmd == "prepare":
        prepare(args)
    elif args.cmd == "train":
        train(args)
    elif args.cmd == "interact":
        interact(args)


if __name__ == "__main__":
    cli()
