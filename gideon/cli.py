import typer
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
    show_about
)
app = typer.Typer()

def about():
            version = "v0.3.0"
            project = get_project_name()
            python_version = get_python_version()
            git_branch = get_git_branch()

            show_about(
                version,
                project,
                python_version,
                git_branch,
            )


commands = {
    "help": show_help,
    "version": show_version,
    "clear": refresh_dashboard,
    "about": show_about


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