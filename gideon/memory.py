import json


def load_memory() -> dict:
    """Load Gideon's long-term memory."""

    with open("memory.json") as file:
        memory = json.load(file)

    return memory

def save_memory(memory: dict) -> None:
    """Save Gideon's memory."""

    with open("memory.json", "w") as file:
        json.dump(memory, file, indent=4)