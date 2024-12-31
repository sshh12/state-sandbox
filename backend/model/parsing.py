import re


def extract_markdown_codeblock(text: str) -> str:
    match = re.search(r"```markdown\n(.*?)```", text, re.DOTALL)
    return match.group(1).strip()
