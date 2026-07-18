import typer
from gideon.config import (
    load_config,
    save_config
)
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


def set_theme():
    config_data = load_config()

    config_data["theme"] = "cyberpunk"

    save_config(config_data)
    print("Theme updated.")



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
        print(f"Unknown setting: {setting}")
        return
    config_data = load_config()

    
    config_data[setting] = value

    save_config(config_data)

    print(f"{setting} updated to {value}.")



commands = {
    "help": show_help,
    "version": show_version,
    "clear": refresh_dashboard,
    "about": show_about,
    "config": config,
    "theme": set_theme

} 

@app.callback(invoke_without_command=True) 

def main() -> None:
    """Start Gideon."""

    show_welcome()

    while True:
        user_input = input("> ").strip().lower()
        parts = user_input.split()

        if not parts:
            continue

        command = parts[0]
       

        if command == "exit":
            print("til next time!")
            break

        
        elif command == "set":
            if len(parts) !=3:
                print("Usage: set <setting> <value>")
            else:
                setting = parts[1]
                value = parts[2]
                set_config(setting, value)
        
        
        elif command in commands:
            commands[command]()
            
            
        else:
            print(f"Unknown command: {command}")



if __name__ == "__main__":
    app()

