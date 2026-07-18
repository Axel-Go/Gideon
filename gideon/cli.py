import typer
from gideon.ai import ask
from gideon.config import (
    load_config,
    save_config
)

from gideon.ui import (
    console, 
    show_help, 
    show_welcome,
    show_version,
    refresh_dashboard,
    show_about,
    show_config,
    show_response
)
app = typer.Typer()


def config():
    config_data = load_config()
    show_config(config_data)

def set_config(setting, value):
    valid_settings = [
        "theme",
        "provider",
        "model",
        "debug",
        "history"
    ]

    if setting not in valid_settings:
        console.print(f"Unknown setting: {setting}")
        return
    config_data = load_config()

    
    config_data[setting] = value

    save_config(config_data)

    console.print(f"{setting} updated to {value}.")



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
        user_input = console.input("[bold cyan]>[/bold cyan] ").strip()

        if not user_input:
            continue

        if user_input.startswith("/"):
            parts = user_input[1:].lower().split()
            if not parts:
                continue
            command = parts[0]
        
        else:
            response = ask(user_input)
            show_response(response)
            continue

        if command == "exit":
            console.print("til next time!")
            break

        
        elif command == "set":
            if len(parts) < 3:
                console.print("Usage: /set <setting> <value>")
            else:
                setting = parts[1]
                value = " ".join(parts[2:])
                set_config(setting, value)
        

        elif command in commands:
            commands[command]()
            
            
        else:
            console.print(f"[red]Unknown command: {command}[/red]")



if __name__ == "__main__":
    app()

