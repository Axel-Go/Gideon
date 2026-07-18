from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
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
            title="v0.3.0",
        )
    )

def show_help() -> None:
    """Display available commands."""

    console.print("[bold cyan]Available Commands[/bold cyan]\n")

    console.print("  /help       Show this help menu")
    console.print("  /version    Show Gideon's version")
    console.print("  /clear      Clear the screen")
    console.print("  /about      About")
    console.print("  /config     Show Gideon's Configuration")
    console.print("  /exit       Exit Gideon")

def show_version() -> None:
    """Display Gideon's current version"""

    console.print("v0.3.0")

def refresh_dashboard() -> None:
    """Refresh Dashboard"""

    console.clear()
    show_welcome()

def show_about() -> None:
    """Display Gideon's Information"""
    
    console.print(
        Panel.fit(
            
            "Name:    Gideon\n"
            "Version: v0.3.0\n"
            "Author:  Axel Go\n"
            "Purpose: Personal AI Assistant\n"
            "Status:  In Development\n",
            title="About Gideon",
        )

    )   

def show_config(config_data) -> None:
    """Display Gideon's Configuration Settings"""
    console.print(
        Panel.fit(
            
            f"Theme: {config_data['theme']}\n"
            f"Provider: {config_data['provider']}\n"
            f"Model: {config_data['model']}\n"
            f"Debug: {config_data['debug']}\n"
            f"History: {config_data['history']}",
            title = "Configuration"

        )
    )
def show_response(response: str) -> None:
    """Display Gideon's response."""

    console.print(Markdown(response))

