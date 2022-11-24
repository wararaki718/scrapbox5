import argparse
import os

import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def get_commandline_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    # Hyperparameters are described here. In this simple example we are just including one hyperparameter.
    parser.add_argument("--max_leaf_nodes", type=int, default=-1)

    # Sagemaker specific arguments. Defaults are set in the environment variables.
    parser.add_argument("--output-data-dir", type=str, default=os.environ["SM_OUTPUT_DATA_DIR"])
    parser.add_argument("--model-dir", type=str, default=os.environ["SM_MODEL_DIR"])
    parser.add_argument("--train", type=str, default=os.environ["SM_CHANNEL_TRAIN"])

    return parser.parse_args()


def main():
    args = get_commandline_args()

    # Take the set of files and read them all into a single pandas dataframe
    input_files = [os.path.join(args.train, file) for file in os.listdir(args.train)]
    if len(input_files) == 0:
        raise ValueError(
            (
                f"There are no files in {args.train}.\n"
                + "This usually indicates that the channel (train) was incorrectly specified,\n"
                + "the data specification in S3 was incorrectly specified or the role specified\n"
                + "does not have permission to access the data."
            )
        )
    raw_data = [pd.read_csv(file, engine="python") for file in input_files]
    train_data = pd.concat(raw_data)

    # labels are in the first column
    train_y = train_data["y"]
    train_X = train_data.drop("y", axis=1)

    # Now use scikit-learn's decision tree classifier to train the model.
    clf = DecisionTreeClassifier(max_leaf_nodes=args.max_leaf_nodes)
    clf = clf.fit(train_X, train_y)

    # Print the coefficients of the trained classifier, and save the coefficients
    joblib.dump(clf, os.path.join(args.model_dir, "model.joblib"))


def model_fn(model_dir: str):
    """Deserialized and return fitted model
    Note that this should have the same name as the serialized model in the main method
    """
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf


if __name__ == "__main__":
    main()
