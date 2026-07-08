import typer
from rich.console import Console
from rich.panel import Panel

app = typer.Typer()
console = Console()


@app.command()
def hello() -> None:
    """Display Gideon's welcome message."""

    console.print(
        Panel.fit(
            "[bold cyan]GIDEON[/bold cyan]\n\n"
            "Hello, Axel.\n"
            "What can i do for you today?",
            title="v0.1.0",
        )
    )


if __name__ == "__main__":
    app()