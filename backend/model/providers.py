from openai import AsyncOpenAI

from config import (
    OPENAI_API_KEY,
    MODEL_HIGH_REASONING,
    MODEL_MEDIUM_REASONING,
    MODEL_LOW_REASONING,
)


class OpenAIProvider:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=OPENAI_API_KEY)

    async def generate_medium_reasoning(self, text: str) -> str:
        response = await self.client.chat.completions.create(
            model=MODEL_MEDIUM_REASONING,
            messages=[{"role": "user", "content": text}],
            reasoning_effort="low",
        )

        return response.choices[0].message.content

    async def generate_high_reasoning(self, text: str) -> str:
        response = await self.client.chat.completions.create(
            model=MODEL_HIGH_REASONING,
            messages=[{"role": "user", "content": text}],
            reasoning_effort="medium",
        )

        return response.choices[0].message.content

    async def generate_low_reasoning(self, text: str) -> str:
        response = await self.client.chat.completions.create(
            model=MODEL_LOW_REASONING,
            messages=[{"role": "user", "content": text}],
            reasoning_effort="low",
        )

        return response.choices[0].message.content
