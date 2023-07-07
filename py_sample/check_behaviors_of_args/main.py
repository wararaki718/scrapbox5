from typing import Any


def sample(**kwargs: Any) -> None:
    metadata = kwargs.pop("metadata", {})
    print(metadata)


def main() -> None:
    sample(metadata={"key": "value"})
    print("DONE")


if __name__ == "__main__":
    main()
