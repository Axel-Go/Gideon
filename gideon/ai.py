import os
from gideon.prompts import SYSTEM_PROMPT
from dotenv import load_dotenv
from google import genai
from google.genai import types
from gideon.memory import (
    load_memory,
    save_memory
)

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask(prompt: str) -> str:
    """Send a prompt to Gemini."""
    
    memory = load_memory()

    if prompt.lower().startswith("remember "):
        fact = prompt[9:]

        memory["notes"] = memory.get("notes", [])
        memory["notes"].append(fact)

        save_memory(memory)

        return "I'll remember that."

    memory_context = f"""
User Information

Name: {memory["user"]["name"]}

Projects:
{", ".join(memory["user"]["projects"])}

Interests:
{", ".join(memory["user"]["interests"])}

Notes:
{", ".join(memory.get("notes",[]))}

"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"{memory_context}\n\nUser: {prompt}",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        ),
    )

    return response.text