import time

from typer import Typer
from rich.progress import track


app = Typer()


@app.command()
def hello(name: str):
    print(f"hello {name}")


@app.command("bye")
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"bye formal {name}")
    else:
        print(f"bye {name}")

@app.command("progress")
def progress():
    total = 0
    for value in track(range(100), description="Processing..."):
        time.sleep(0.01)
        total += 1
    print(total)


if __name__ == "__main__":
    app()
