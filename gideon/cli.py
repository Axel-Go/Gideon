import typer

from gideon.ui import (
    console, 
    show_help, 
    show_welcome,
    show_version,
    refresh_dashboard
)
app = typer.Typer()


commands = {
    "help": show_help,
    "version": show_version,
    "clear": refresh_dashboard,


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