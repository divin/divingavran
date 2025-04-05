from typing import Any

import yaml


def read_yaml(file: str) -> Any:
    """Read a YAML file and return its content.

    Args:
        file (str): The path to the YAML file.

    Returns:
        Any: The content of the YAML file.
    """
    with open(file=file, mode="r") as stream:
        try:
            content: Any = yaml.safe_load(stream=stream)
        except yaml.YAMLError as error:
            raise error

    return content


def read_markdown_file(file: str, number_of_lines: int | None = None) -> str:
    """Read a markdown file and return its content.

    Args:
        file (str): The path to the markdown file.

    Returns:
        str: The content of the markdown file.
    """
    with open(file=file, mode="r") as markdown_file:
        if number_of_lines:
            return "".join(list(markdown_file)[:number_of_lines])

        return markdown_file.read()
