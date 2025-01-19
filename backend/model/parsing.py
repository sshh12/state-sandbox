import re
import markdown_to_json
from typing import Any, List, Tuple, Dict


def extract_codeblock(text: str) -> str:
    match = re.search(r"```[a-zA-Z]+\n(.*?)```", text, re.DOTALL)
    return match.group(1).strip()


def extract_markdown_section(markdown_text: str, h1_header_name: str) -> str:
    """
    Extracts content under a specific h1 header from markdown text.

    Args:
        markdown_text (str): The full markdown text to parse
        h1_header_name (str): The name of the h1 header to find

    Returns:
        str: The content under the specified header, or empty string if not found

    Example:
        ```markdown
        # Header1
        - a
        - b
        - c

        # Header2
        other content
        ```
        extract_markdown_section(text, "Header1") -> "\n- a\n- b\n- c\n"
    """
    # Split the text into lines
    lines = markdown_text.splitlines()

    # Find the target header
    target_header = f"# {h1_header_name}"

    # Variables to track extraction
    content = []
    is_capturing = False

    for line in lines:
        # Check if we've hit the target header
        if line.strip() == target_header:
            is_capturing = True
            continue

        # Stop capturing if we hit another h1 header
        if line.strip().startswith("# ") and is_capturing:
            break

        # Capture content if we're in the right section
        if is_capturing:
            content.append(line)

    # Join captured lines and return
    return "\n".join(content).strip() + "\n"


def _md_to_json(markdown: str) -> dict:
    # Remove HTML comments
    markdown = re.sub(r"<!--.*?-->", "", markdown, flags=re.DOTALL)
    return markdown_to_json.dictify(markdown)


def _parse_unit(value: str) -> dict:
    result = {"raw": value, "unit": None, "value": value}
    if match := re.match(r"\$?(\d+(?:,\d{3})*(?:\.\d+)?)\s*(.*)", value):
        value_part, unit = match.groups()
        cleaned_value = value_part.replace(",", "")
        numeric_value = float(cleaned_value)
        result = {
            "value": numeric_value,
            "unit": unit or "units",
            "raw": value,
        }
    elif match := re.match(r"(\d+)%", value):
        numeric_value = int(match.group(1))
        result = {
            "value": numeric_value,
            "unit": "%",
            "raw": value,
        }
    if result["unit"] == "%":
        result["value"] = result["value"] / 100.0
    return result


def _clean_key(key: str) -> str:
    key = key.lower()
    key = re.sub(r"[^a-zA-Z ]", "", key).strip().replace(" ", "_")
    return key


def _parse_kv(data: Any, parent_key: str = "") -> Any:
    """
    Recursively parse the data, converting "Key: Value" strings into proper key-value pairs

    Handles:
    - Dictionary values
    - List values
    - "Key: Value" strings
    """
    if isinstance(data, dict):
        new_data = {}
        for key, value in data.items():
            # Recursively parse nested structures
            parsed_value = _parse_kv(value, key)

            # Handle string keys with colons
            if isinstance(key, str) and ":" in key:
                key = key.split(":", 1)[0].strip()

            new_data[_clean_key(key)] = parsed_value
        return new_data

    elif isinstance(data, list):
        # Handle lists by parsing each element and merge dicts
        parsed_items = [_parse_kv(item, parent_key) for item in data]

        # If all items are dicts, merge them
        if all(isinstance(item, dict) for item in parsed_items):
            merged = {}
            for item in parsed_items:
                merged.update(item)
            return merged

        return parsed_items

    elif (
        isinstance(data, str)
        and ":" in data
        and not parent_key.endswith(" System")
        and not parent_key.endswith(" Headlines")
    ):
        # Parse "Key: Value" strings
        key, value = data.split(":", 1)
        return {_clean_key(key.strip()): {**_parse_unit(value.strip()), "key": key}}

    return data


def parse_state(state_markdown: str) -> dict:
    data = _md_to_json(state_markdown)
    data = _parse_kv(data)
    return data


def parse_events_section(section: str) -> List[Tuple[float, str]]:
    """Parse a section of events into a list of (probability, event) tuples."""
    events = []
    for line in section.strip().split("\n"):
        if not line.startswith("- "):
            continue
        try:
            prob_str, event = line[2:].split("%", 1)
            prob = float(prob_str.strip()) / 100
            events.append((prob, event.strip()))
        except Exception:
            continue
    return events


def parse_events_output(output: str) -> Dict[str, List[Tuple[float, str]]]:
    """Parse the full events output into a dictionary of category -> events list."""
    categories = {}
    current_category = None
    current_events = []

    for line in output.split("\n"):
        line = line.strip()
        if not line:
            continue

        if line.startswith("# "):
            if current_category and current_events:
                categories[current_category] = parse_events_section(
                    "\n".join(current_events)
                )
            current_category = line[2:]
            current_events = []
        else:
            current_events.append(line)

    if current_category and current_events:
        categories[current_category] = parse_events_section("\n".join(current_events))

    return categories
