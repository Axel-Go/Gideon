from rich.console import Console
from rich.panel import Panel
from gideon.system import get_project_name
from gideon.system import (
    get_project_name,
    get_python_version,
    get_git_branch,
)

console = Console()


def show_welcome() -> None:
    """Display Gideon's welcome screen."""

    console.print(
        Panel.fit(
            "[bold cyan]GIDEON[/bold cyan]\n\n"
            f"Project: {get_project_name()}\n"
            f"Python: {get_python_version()}\n"
            f"Branch: {get_git_branch()}\n\n"
            "Hello Axel, What can i do for you today?",
            title="v0.1.0",
        )
    )