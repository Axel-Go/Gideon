from rich.console import Console
from rich.panel import Panel

console = Console()


def show_welcome() -> None:
    """Display Gideon's welcome screen."""

    console.print(
        Panel.fit(
            "[bold cyan]GIDEON[/bold cyan]\n\n"
            "Welcome, Axel.\n"
            "What can i do for you today?",
            title="v0.1.0",
        )
    )