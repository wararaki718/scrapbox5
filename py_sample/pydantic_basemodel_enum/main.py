from schema import User, AnimalEnum, AgeEnum


def main() -> None:
    user = User(
        name="test",
        animal=AnimalEnum.cat,
        age=AgeEnum.one
    )
    print(user)

    user2 = User(
        name="sample",
        animal="dog",
        age=2
    )
    print(user2)
    print("DONE")


if __name__ == "__main__":
    main()
