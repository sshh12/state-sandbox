from openai import AsyncOpenAI

from config import OPENAI_API_KEY


class OpenAIProvider:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=OPENAI_API_KEY)

    async def generate_fast_reasoning(self, text: str) -> str:
        response = await self.client.chat.completions.create(
            model="o1-mini",
            messages=[{"role": "user", "content": text}],
        )
        return response.choices[0].message.content
