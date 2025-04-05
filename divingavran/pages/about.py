import reflex as rx

from divingavran.constants import MARKDOWN_PARAMS
from divingavran.layouts.default import default_layout
from divingavran.utilities import read_markdown_file


def about() -> rx.Component:
    content = read_markdown_file("content/about.md")
    return default_layout(
        title="About 🙋",
        components=[
            rx.markdown(
                content,
                **MARKDOWN_PARAMS,  # type: ignore
            ),
        ],
    )
