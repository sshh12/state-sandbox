from typing import List, Tuple
from datetime import datetime
from model.providers import OpenAIProvider
from model.prompts import STATE_TEMPLATE, DIFF_EXECUTIVE_TEMPLATE
from model.parsing import extract_markdown_codeblock, extract_svg_codeblock
import asyncio


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


async def generate_state_flag(state: str) -> str:
    provider = OpenAIProvider()
    prompt = f"""
Given this fictional state, generate a flag for it. 

Consider and reason on the relationship between the colors, symbols, and organization of the flag and the nature of the country.

<state>
{state}
</state>

<example>
```svg
<svg xmlns="http://www.w3.org/2000/svg" width="900" height="600">
   <!-- Background -->
   ...
   <!-- Symbols -->
   ...
</svg>
```
</example>

Reply with the flag in an SVG codeblock.
- You must make the width = 900 and height = 600
""".strip()
    output = await provider.generate_fast_reasoning(prompt)
    return extract_svg_codeblock(output)


async def generate_state(date: str, name: str, questions: List[Tuple[str, int]]) -> str:
    provider = OpenAIProvider()
    prompt = f"""
Fill out the following template for a fictional country in {_format_month_date(date)}.

<state-template>
{STATE_TEMPLATE}
</state-template>

<values>
Suggested Country Name: {name[:30]} (ignore if this already exists, make it more realistic, e.g. Republic of, -istan, -land, etc)

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
2. The full <state-template> in a markdown codeblock. Do not include xml tags.
"""
    output = await provider.generate_fast_reasoning(prompt)
    return extract_markdown_codeblock(output)


async def generate_next_state(
    start_date: datetime, end_date: datetime, prev_state: str, policy: str
) -> Tuple[str, str]:
    provider = OpenAIProvider()
    diff_prompt = f"""
Given this fictional state and the following events between {start_date} and {end_date}, simulate the key changes that occur to the state.

<state>
{prev_state}
</state>

<events>
- {policy}
</events>

You must jointly consider:
- All <events> along with their impact on the economy, society, and international relations (all aspects of the <state>)
- The unique characteristics, systems, and values of the <state>
- Natural changes in population and resource counts over the course of a month
- Natural random changes in production, distributions, infrastructure, and facilities.

Think carefully and consider the full and holistic effects of all events along with natural expected changes and variance overtime. For this simulation to be accurate you must consider not only the immediate impacts but the higher order consequences.

Reply with:
1. The high-level natural expected changes and random changes during the month.
2. For each event, the high-level expected impacted on the <state>
- Some events will be very impactful and others might have minimal change
- Event impacts can span several state dimensions with complex higher-order consequences
3. For each state dimension (Overview, People, Education, ...) list out the explicit changes. 
- Noting what changed (before/after), what's added, and what's removed. 
- Providing explicit numerical or percentage values before before/after.
- Noting how the top challenges in each dimension might evolve
- Noting for critical changed metrics (e.g. GDP, inflation, etc) how you computed the signficance of the change 
""".strip()
    diff_output = await provider.generate_fast_reasoning(diff_prompt)
    print(diff_output)
    new_state_prompt = f"""
Given this fictional state and the following events between {start_date} and {end_date}, provide the updated <state>.

<state-template>
{STATE_TEMPLATE}
</state-template>

<state>
{prev_state}
</state>

<state-recent-changes>
{diff_output}
</state-recent-changes>

The impacts of recent events have already been decided in <state-recent-changes>. 

Your task is to return <state> in <state-template> with the changes from <state-recent-changes> applied. 

Note that <state-recent-changes> might not be in the right format. 

Reply with the new <state> in a markdown codeblock. Do not include xml tags.
""".strip()
    new_state_output = extract_markdown_codeblock(
        await provider.generate_fast_reasoning(new_state_prompt)
    )
    new_state_report_prompt = f"""
Given this fictional state and the following events between {start_date} and {end_date}, provide a report on the changes in the state.

<original-state>
{prev_state}
</original-state>

<state-recent-changes>
{diff_output}
</state-recent-changes>

<report-template>
{DIFF_EXECUTIVE_TEMPLATE}
</report-template>

Reply with a markdown codeblock containing the report. Do not include xml tags.
""".strip()
    new_state_report = extract_markdown_codeblock(
        await provider.generate_fast_reasoning(new_state_report_prompt)
    )
    print(new_state_output)
    print(new_state_report)
    return new_state_output, new_state_report
