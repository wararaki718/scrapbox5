from pathlib import Path

from user import User


def main():
    filepath = Path("./user.yaml")
    users = User.load(filepath)

    for user in users:
        print(user)
    
    print("DONE")


if __name__ == "__main__":
    main()
