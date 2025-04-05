import reflex as rx

from divingavran.constants import MARKDOWN_PARAMS
from divingavran.layouts.default import default_layout
from divingavran.utilities import read_markdown_file


def error() -> rx.Component:
    content = read_markdown_file("content/404.md")
    return default_layout(
        title="404 😑",
        components=[
            rx.markdown(
                content,
                **MARKDOWN_PARAMS,  # type: ignore
            ),
        ],
    )
