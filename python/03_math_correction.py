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


SYSTEM_PROMPT = ""

# Prompt
PROMPT = """
如下结论对吗？

2x - 3 = 9
2x = 6
x = 3"""
print(get_completion(PROMPT, SYSTEM_PROMPT))
