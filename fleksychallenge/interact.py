import os

import spacy


def interact(args):
    """Function for the user to interact with a trained model.

    After loading the trained model, this function will keep asking the user
    to input some text (the tweet to analyze), and it will return the
    classification score for each sentiment.

    Args:
        args (argparse.Namespace): CLI arguments.
    """
    # Load our model
    sentiment_model = spacy.load(os.path.join(args.model, "model-best"))

    text = ""
    while text != "qq":
        text = input("Type a tweet followed by Enter to analyze its sentiment, or `qq` for leaving :")
        if x == "qq":
            break
        elif len(x) == 0:
            print("Coudln't detect any input... Type `qq` if you want to leave")
        else:
            out = sentiment_model(preprocess({"text": x})["text"])
            print(out.cats)

    print("Bye ~")
