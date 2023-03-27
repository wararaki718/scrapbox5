from pathlib import Path

import joblib
import pandas as pd


def load_pickle_df(filepath: Path) -> pd.DataFrame:
    df = pd.DataFrame()
    if filepath.exists():
        try:
            df = pd.read_pickle(filepath)
            print(f"{filepath} loaded!")
        except Exception as e:
            print(f"Failed to load {filepath}")
    else:
        print(f"{filepath} is not existed")

    return df


def load_joblib_df(filepath: Path) -> pd.DataFrame:
    df = pd.DataFrame()
    if filepath.exists():
        try:
            tmp = joblib.load(filepath)
            df = pd.DataFrame(tmp)
            print(f"{filepath} loaded! (type: {type(df)})")
        except Exception as e:
            print(f"Failed to load {filepath}")
    else:
        print(f"{filepath} is not existed")
    return df


def show(df: pd.DataFrame, filepath: Path):
    print(f"{filepath}: {df.shape}")
    print()


def main():
    pkl36_path = Path("/data/binary36.pkl")
    pkl37_path = Path("/data/binary37.pkl")
    pkl38_path = Path("/data/binary38.pkl")
    joblib36_path = Path("/data/binary36.joblib")
    joblib37_path = Path("/data/binary37.joblib")
    joblib38_path = Path("/data/binary38.joblib")

    print("## data load")
    df = load_pickle_df(pkl36_path)
    show(df, pkl36_path)

    df = load_pickle_df(pkl38_path)
    show(df, pkl38_path)

    df = load_joblib_df(joblib36_path)
    show(df, joblib36_path)

    df = load_joblib_df(joblib38_path)
    show(df, joblib38_path)

    print("## data dump")
    df = pd.read_csv("/csvs/sample.csv")
    df.to_pickle(pkl38_path)
    print(f"'{pkl38_path}' was created")

    tmp = df.to_dict(orient="records")
    joblib.dump(tmp, joblib38_path)
    print(f"'{joblib38_path}' was created")
    
    print("DONE")


if __name__ == "__main__":
    main()
