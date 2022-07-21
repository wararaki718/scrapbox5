import typer


def main(name: str = typer.Option("test")):
    print(f"test {name}")
    print("DONE")


if __name__ == "__main__":
    typer.run(main)
