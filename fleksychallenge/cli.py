import argparse

from fleksychallenge import interact, prepare, train


def cli():
    parser = argparse.ArgumentParser(description="Fleksy challenge part 1")
    parser.add_argument("cmd", help="Command to execute", choices=["prepare", "train", "interact"])
    parser.add_argument("--dataset", help="Where to save/load the dataset from", default="tweet_dataset")
    parser.add_argument("--config", help="Location of the config file to use for training", default="config.cfg")
    parser.add_argument("--model", help="Where to save/load the model from", default="sentiment_model")
    parser.add_argument("--gpu", action="store_true")
    args = parser.parse_args()

    if args.cmd == "prepare":
        prepare(args)
    elif args.cmd == "train":
        train(args)
    elif args.cmd == "interact":
        interact(args)


if __name__ == "__main__":
    cli()
