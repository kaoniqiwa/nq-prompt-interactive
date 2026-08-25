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
    return bool(re.search(r"giggles", text) or re.search(r"soo", text))


SYSTEM_PROMPT = "you are a 3 year old child"

# Prompt
PROMPT = "How big is the sky?"
response = get_completion(PROMPT, SYSTEM_PROMPT)

print(response)
print("\n--------------------------- GRADING ---------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))
