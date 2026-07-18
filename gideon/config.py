import json


def load_config() -> dict:
    """Load Gideon's configuration."""

    with open("config.json") as file:
        config = json.load(file)

    return config

def save_config(config_data) -> None:
    """Save Gideon's configuration."""

    with open("config.json","w") as file:
        json.dump(config_data, file, indent=4)
