import typer


def app1(name: str = typer.Option(..., "--first-name")):
    print(f"[app1] hello, {name}")


# does not run
def app2(name: str = typer.Option(..., "--last-name")):
    print(f"[app2] hello, {name}")


def main():
    typer.run(app1)
    typer.run(app2)


if __name__ == "__main__":
    main()
