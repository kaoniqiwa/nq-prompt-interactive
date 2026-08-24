from os import environ

from anthropic import Anthropic

base_url = environ.get("ANTHROPIC_BASE_URL", "http://localhost:11434")
api_key = environ.get("ANTHROPIC_API_KEY", "ollama")
model = environ.get("ANTHROPIC_MODEL", "deepseek-r1:8b")

client = Anthropic(base_url=base_url, api_key=api_key)


def get_completion(prompt: str):
    message = client.messages.create(
        model=model,
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )
    for block in message.content:
        if block.type == "text":
            print(block.text)


get_completion("你是谁？")
