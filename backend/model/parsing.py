import re
import markdown_to_json
from typing import Any, List, Tuple, Dict, Optional


def extract_codeblock(text: str, fix_markdown: bool = True) -> str:
    match = re.search(r"```[a-zA-Z]+\n(.*?)```", text, re.DOTALL)
    out = match.group(1).strip()
    if fix_markdown:
        # remove italic, bold, etc.
        out = re.sub(r"_(.*?)_", r"\1", out)
        out = re.sub(r"\*(.*?)\*", r"\1", out)
        out = out.replace("\\$", "$")
        out = _fix_compositions(out)
    return out


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

    # Define multipliers for different scales
    multipliers = {
        "trillion": 1e12,
        "billion": 1e9,
        "million": 1e6,
        "thousand": 1e3,
        "k": 1e3,
    }

    if match := re.match(r"\$?(\d+(?:,\d{3})*(?:\.\d+)?)\s*(.*)", value):
        value_part, unit = match.groups()
        cleaned_value = value_part.replace(",", "")
        numeric_value = float(cleaned_value)

        # Split unit into parts (e.g., "billion dollars" -> ["billion", "dollars"])
        unit_parts = unit.lower().split()

        # Check if first part is a multiplier
        if unit_parts and unit_parts[0] in multipliers:
            numeric_value *= multipliers[unit_parts[0]]
            unit = " ".join(unit_parts[1:]) if len(unit_parts) > 1 else "units"

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


_PARAGRAPH_SUFFIXES = [
    " System",
    " Practices",
    " Identity",
    " Features",
    " Participation",
    "Technologies",
]

_LIST_PARAGRAPH_SUFFIXES = [" Headlines", " Quotes"]


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

    elif isinstance(data, list) and not parent_key.endswith(tuple(_PARAGRAPH_SUFFIXES)):
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
        and not parent_key.endswith(
            tuple(_PARAGRAPH_SUFFIXES + _LIST_PARAGRAPH_SUFFIXES)
        )
    ):
        # Parse "Key: Value" strings
        key, value = data.split(":", 1)
        return {_clean_key(key.strip()): {**_parse_unit(value.strip()), "key": key}}

    if isinstance(data, list):
        data = "\n".join(["- " + item for item in data])

    return data


def _get_nested_value(data: dict, key_path: str):
    """Helper function to get nested dictionary value using dot notation."""
    keys = key_path.split(".")
    current = data
    for key in keys:
        if not isinstance(current, dict):
            return None
        if key not in current:
            return None
        current = current[key]
    return current


def _filter_dict_by_keys(data: dict, only_keys: List[str]) -> dict:
    """Filter dictionary to only include specified nested keys."""
    result = {}
    for key_path in only_keys:
        keys = key_path.split(".")
        current = result
        value = _get_nested_value(data, key_path)
        if value is not None:
            # Build nested structure
            for key in keys[:-1]:
                current = current.setdefault(key, {})
            current[keys[-1]] = value
    return result


def parse_state(state_markdown: str, only_keys: Optional[List[str]] = None) -> dict:
    data = _md_to_json(state_markdown)
    data = _parse_kv(data)
    if only_keys:
        data = _filter_dict_by_keys(data, only_keys)
    return data


def _parse_events_section(section: str) -> List[Tuple[float, str]]:
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
                categories[current_category] = _parse_events_section(
                    "\n".join(current_events)
                )
            current_category = line[2:]
            current_events = []
        else:
            current_events.append(line)

    if current_category and current_events:
        categories[current_category] = _parse_events_section("\n".join(current_events))

    return categories


def _fix_compositions(markdown: str) -> str:
    """Find sections with "Composition" in their headers and normalize the percentages to sum to 100%."""
    lines = markdown.split("\n")
    output_lines = []

    in_composition = False
    composition_items = []
    composition_start_index = -1

    for i, line in enumerate(lines):
        # Check for composition section headers
        if line.startswith(("#", "###", "####")) and "Composition" in line:
            # If we were already in a composition section, normalize and add it
            if in_composition:
                normalized_lines = _normalize_percentages(composition_items)
                output_lines.extend(normalized_lines)
                composition_items = []

            in_composition = True
            composition_start_index = i
            output_lines.append(line)
            continue

        # Check for end of composition section (next header or blank line after items)
        if in_composition and (
            line.startswith("#") or (line.strip() == "" and composition_items)
        ):
            normalized_lines = _normalize_percentages(composition_items)
            output_lines.extend(normalized_lines)
            composition_items = []
            in_composition = False
            if line.strip():  # Only add non-empty lines
                output_lines.append(line)
            continue

        # Collect composition items
        if in_composition and line.startswith("- ") and "%" in line:
            composition_items.append(line)
        else:
            output_lines.append(line)

    # Handle case where composition section is at end of file
    if in_composition and composition_items:
        normalized_lines = _normalize_percentages(composition_items)
        output_lines.extend(normalized_lines)

    return "\n".join(output_lines)


def _normalize_percentages(items: list[str]) -> list[str]:
    """Helper function to normalize percentages in a list of items to sum to 100%."""
    if not items:
        return []

    # Extract values and labels
    parsed_items = []
    total = 0

    for item in items:
        try:
            # Extract percentage value
            label, value = item[2:].rsplit(":", 1)
            value = float(value.strip().rstrip("%"))
            total += value
            parsed_items.append((label, value))
        except (ValueError, IndexError):
            continue

    if not parsed_items or total == 0:
        return items

    # Normalize values to sum to 100%
    scale_factor = 100.0 / total
    normalized_items = []

    for label, value in parsed_items:
        new_value = value * scale_factor
        # Format with 1 decimal place if needed, otherwise as integer
        if new_value == int(new_value):
            value_str = f"{int(new_value)}%"
        else:
            value_str = f"{new_value:.1f}%"
        normalized_items.append(f"- {label}: {value_str}")

    return normalized_items
