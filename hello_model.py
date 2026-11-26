"""Day 1: talk to a model.

Calls a chat model on GitHub Models (free) with the openai SDK and prints
the answer plus token usage. The same code works against Azure OpenAI /
Foundry later by changing the base URL, key and model name.

Usage:
    python day01/hello_model.py "Explain what an LLM is to a DevOps engineer"
"""

import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

ENDPOINT = os.getenv("MODEL_ENDPOINT", "https://models.github.ai/inference")
MODEL = os.getenv("MODEL_NAME", "openai/gpt-4.1-mini")
TOKEN = os.getenv("GITHUB_TOKEN")

SYSTEM_PROMPT = (
    "You are a senior DevOps engineer. Answer briefly, in plain language, "
    "and use DevOps analogies where they help."
)


def ask(question: str, temperature: float = 0.2, max_tokens: int = 400) -> None:
    if not TOKEN:
        sys.exit("GITHUB_TOKEN is not set. Copy .env.example to .env and add your token.")

    client = OpenAI(base_url=ENDPOINT, api_key=TOKEN)
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )

    print(response.choices[0].message.content)
    usage = response.usage
    print(
        f"\n--- model: {MODEL} | tokens in: {usage.prompt_tokens} "
        f"| out: {usage.completion_tokens} | total: {usage.total_tokens}"
    )


if __name__ == "__main__":
    question = " ".join(sys.argv[1:]) or "In 3 sentences: what is an LLM, in DevOps terms?"
    ask(question)
