import re
from os import environ

from anthropic import Anthropic
from extract import extract_text_from_message

base_url = environ.get("ANTHROPIC_BASE_URL", "http://localhost:11434")
api_key = environ.get("ANTHROPIC_API_KEY", "ollama")
model = environ.get("ANTHROPIC_MODEL", "deepseek-r1:8b")

client = Anthropic(base_url=base_url, api_key=api_key)


def get_completion(prompt: str, system_prompt=""):
    message = client.messages.create(
        model=model,
        max_tokens=2000,
        system=system_prompt,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    return extract_text_from_message(message)


# Function to grade exercise correctness
def grade_exercise(text):
    return text == "Michael Jordan"


# Prompt
PROMPT = "Who is the best basketball player of all time? Yes, there are differing opinions, but if you absolutely had to pick one player, who would it be?Just give me the name"
SYSTEM_PROMPT = ""

response = get_completion(PROMPT, SYSTEM_PROMPT)


# Print Claude's response and the corresponding grade
print(response)
print("\n--------------------------- GRADING ---------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))
