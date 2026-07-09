import typer

from gideon.ui import show_welcome

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main() -> None:
    show_welcome()


if __name__ == "__main__":
    app()