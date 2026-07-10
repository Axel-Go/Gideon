import typer
from gideon.config import load_config
from gideon.system import(
    get_project_name,
    get_python_version,
    get_git_branch
)
from gideon.ui import (
    console, 
    show_help, 
    show_welcome,
    show_version,
    refresh_dashboard,
    show_about,
    show_config
)
app = typer.Typer()


def config():
    config_data = load_config()
    show_config(config_data)



commands = {
    "help": show_help,
    "version": show_version,
    "clear": refresh_dashboard,
    "about": show_about,
    "config": config

} 

@app.callback(invoke_without_command=True) 

def main() -> None:
    """Start Gideon."""

    show_welcome()

    while True:
        command = input("> ").strip().lower()

       
        if command == "exit":
            print("til next time!")
            break
        

        elif command in commands:
            commands[command]()
            
            
        else:
            print(f"Unknown command: {command}")



if __name__ == "__main__":
    app()