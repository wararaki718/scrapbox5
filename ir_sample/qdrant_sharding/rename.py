import shutil
from pathlib import Path


def main():
    latest = sorted(Path("./snapshots/reviews").glob("*.snapshot"))[-1]
    after = Path("./snapshots/reviews.snapshot")

    shutil.copy(latest, after)
    print("DONE")


if __name__ == "__main__":
    main()
