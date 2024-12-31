from typing import List, Tuple
from datetime import datetime
from model.providers import OpenAIProvider
from model.prompts import STATE_TEMPLATE
from model.parsing import extract_markdown_codeblock


def _format_month_date(date: str) -> str:
    return datetime.strptime(date, "%Y-%m").strftime("%B %Y")


def _format_questions(questions: List[Tuple[str, int]]) -> str:
    value_to_text = {
        1: "Strongly Disagree",
        2: "Disagree",
        3: "Neutral",
        4: "Agree",
        5: "Strongly Agree",
    }
    return "\n".join([f"- {q[0]}: {value_to_text[q[1]]}" for q in questions])


async def generate_state(date: str, name: str, questions: List[Tuple[str, int]]) -> str:
    provider = OpenAIProvider()
    prompt = f"""
Fill out the following template for a fictional country in {_format_month_date(date)}.

<state-template>
{STATE_TEMPLATE}
</state-template>

<values>
Suggested Country Name: {name[:30]} (ignore if this already exists)

{_format_questions(questions)}
</values>

- Choose a unique but realistic name taking into account the <values> above. It should NOT be an existing nation or from a well-known fictional universe.
- Include a single fictional country-specific ethnic group and use real groups for the others (e.g. White, Asian, etc)
- Include a single fictional country-specific religious group and use real religions for the others (e.g. Christianity, Islam, etc)
- Use real life countries for import and export partners
- Assume population of 25 million, area of 500k sq km area, and initial GDP of 2.0 billion USD
- Be realistic and balanced based on what you know about the world while being creative with your choice of government type (overfitting the values above), systems (health care, justice, etc), and the challenges for each section.
- When planning, consider the impacts of the <values> above on policies, government, culture, heath, justice, and the economy

Reply with:
1. A brief summary of how the <values> above influence the dimensions of the state, how you will balance their strengths and flaws, and what makes them unique in the world.
2. The full <state-template> in a markdown codeblock
"""
    output = await provider.generate_fast_reasoning(prompt)
    return extract_markdown_codeblock(output)
