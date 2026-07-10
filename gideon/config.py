import json


def load_config() -> dict:
    """Load Gideon's configuration."""

    with open("config.json") as file:
        config = json.load(file)

    return config