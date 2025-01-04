from typing import List, Tuple
from datetime import datetime
import random
from model.providers import OpenAIProvider
from model.prompts import STATE_TEMPLATE, DIFF_EXECUTIVE_TEMPLATE, RANDOM_TEMPLATE
from model.parsing import (
    extract_markdown_codeblock,
    extract_svg_codeblock,
    parse_events_output,
)


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

Consider and reason on the relationship between the colors, symbols, and organization of the flag and the nature and values of the country.

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

Reply with:
(1) A brief summary of how the the states unique values, culture, and systems are will be represented in the flag.
(2) The flag in an SVG codeblock.
- You must make the width = 900 and height = 600
""".strip()
    output = await provider.generate_fast_reasoning(prompt)
    return extract_svg_codeblock(output)


async def generate_state(date: str, name: str, questions: List[Tuple[str, int]]) -> str:
    provider = OpenAIProvider()
    prompt = f"""
Fill out the following template for a fictional country in {_format_month_date(date)}.

Suggested Country Name: {repr(name[:30])} (make it more realistic, e.g. Republic/Federation/Empire/Kingdom/Sultanate/Emirates/Commonwealth of, -ia/-istan/-onia, etc)

<state-template>
{STATE_TEMPLATE}
</state-template>

<values>
{_format_questions(questions)}
</values>

- Choose a unique but realistic name taking into account suggested name above. It should NOT be an existing nation or from a well-known fictional universe.
- Include a single fictional country-specific ethnic group and use real groups for the others (e.g. White, Asian, etc)
- Include a single fictional country-specific religious group and use real religions for the others (e.g. Christianity, Islam, etc)
- Use real countries (e.g. USA, China, Russia, etc) for import and export partners
- Assume population of 25.68 million, area of 520k sq km area, and initial GDP of 2,700,000,000 USD
- Be realistic and balanced based on what you know about the world while being creative with your choice of government type (overfitting the values above), systems (health care, justice, etc), and the challenges for each section.
- When planning, consider the impacts of the <values> above on policies, government, culture, heath, justice, and the economy

Reply with:
1. A brief summary of how the <values> above influence the dimensions of the state, how you will balance their strengths and flaws, and what makes them unique in the world.
2. The full <state-template> in a markdown codeblock. Do not include xml tags.
"""
    output = await provider.generate_fast_reasoning(prompt)
    return extract_markdown_codeblock(output)


async def generate_diff_report(
    start_date: datetime, end_date: datetime, prev_state: str, diff_output: str
) -> str:
    provider = OpenAIProvider()
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
        await provider.generate_fast(new_state_report_prompt)
    )
    return new_state_report


def _sample_event(events: List[Tuple[float, str]]) -> str:
    """Sample a single event based on probabilities."""
    total = sum(prob for prob, _ in events)
    r = random.random() * total
    cumsum = 0
    for prob, event in events:
        cumsum += prob
        if r <= cumsum:
            return event
    return events[-1][1]  # Fallback to last event


async def generate_random_events(
    start_date: datetime,
    end_date: datetime,
    prev_state: str,
    historical_events_str: str,
) -> List[str]:
    provider = OpenAIProvider()
    prompt = f"""
Given this fictional state from {start_date} to {end_date}, provide a realistic list of potential random events that could occur within the next year in the correct format.

<format>
{RANDOM_TEMPLATE}
</format>
        
<state>
{prev_state}
</state>

<historical-events>
{historical_events_str}
</historical-events>

Reply with <format> within a markdown codeblock. Do not include xml tags.
""".strip()
    output = extract_markdown_codeblock(await provider.generate_fast_reasoning(prompt))

    # Parse the output into categories and their events
    categories = parse_events_output(output)

    # Sample one event from each category
    sampled_events = []
    for category, events in categories.items():
        event = _sample_event(events)
        sampled_events.append(f"{category}: {event}")

    return sampled_events


async def generate_next_state(
    start_date: datetime,
    end_date: datetime,
    prev_state: str,
    policy: str,
    historical_events: List[Tuple[str, List[str]]] = None,
) -> Tuple[str, str, str]:
    provider = OpenAIProvider()

    historical_events_str = "No notable historical events"
    if historical_events:
        historical_events_str = "\n".join(
            [f"{date}:\n" + "\n".join(events) for date, events in historical_events]
        )

    events = await generate_random_events(
        start_date, end_date, prev_state, historical_events_str
    )
    events_str = "\n".join([f"- {e}" for e in events])
    events_str = f"- Government Events: {policy if policy else 'None'}\n{events_str}"
    print(historical_events_str)
    print(events_str)

    diff_prompt = f"""
Given this fictional state and the following events between {start_date} and {end_date}, simulate the key changes that occur to the state.

<state>
{prev_state}
</state>

<historical-events>
{historical_events_str}
</historical-events>

<recent-events>
{events_str}
</recent-events>

You must jointly consider:
- All <recent-events> along with their impact on the economy, society, and international relations (all aspects of the <state>)
- The historical events and their long-term effects on the current state
- The unique characteristics, systems, and values of the <state>
- Natural changes in population and resource counts over the course of a year
- Natural random changes in production, distributions, infrastructure, facilities, and other metrics.

Think carefully and consider the full and holistic effects of all events along with natural expected changes and variance overtime. For this simulation to be accurate you must consider not only the immediate impacts but the higher order consequences.

Reply with:
1. The high-level natural expected changes and random changes during the year. Nearly ALL numerical metrics should change at least slightly.
2. For each event, the high-level expected impacted on the <state>
- Some events will be very impactful and others might have minimal change
- Event impacts can span several state dimensions with complex higher-order consequences
- Government policies (if any) should, no matter how positive, include complex negative consequences
3. For each state dimension (Overview, People, Education, ...) list out the explicit changes. 
- Noting what changed (before/after), what's added, and what's removed. 
- Providing explicit numerical or percentage values before before/after.
- Noting how the top challenges in each dimension might evolve
- Noting for critical changed metrics (e.g. GDP, inflation, etc) how you computed the signficance of the change 
(do not include a summary at the end)
""".strip()
    diff_output = await provider.generate_strong_reasoning(diff_prompt)

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
- For dimension challenges, lean towards adding a challenge and only remove a challenge if it's no longer relevant.
- For government policies, lean towards adding a policy and only remove a policy if it's no longer relevant.
- Recompute all percentages to add up to 100%
""".strip()
    print(diff_output)
    new_state_output = extract_markdown_codeblock(
        await provider.generate_fast_reasoning(new_state_prompt)
    )
    print(new_state_output)
    return diff_output, new_state_output, events_str


async def generate_state_advice(state: str, question: str) -> str:
    provider = OpenAIProvider()
    prompt = f"""
You are an expert advisor for the government of a fictional country. Given the user's question (the head of state), provide advice for their policies.

<state>
{state}
</state>

<question>
{question}
</question>

Reply with a markdown codeblock containing the advice. Do not include xml tags.

Format policy advice in an imperative format:
- "Create a restriction on ..."
- "Ban the use of ..."
- "Increase the minimum wage to ..."

Be brief, technical, and concise. If writing out suggested policies, limit it to the top 3 most effective ones.
""".strip()
    output = await provider.generate_fast(prompt)
    return extract_markdown_codeblock(output)
