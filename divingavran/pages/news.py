import reflex as rx

from divingavran.constants import MARKDOWN_PARAMS
from divingavran.layouts.default import default_layout
from divingavran.utilities import read_markdown_file


def news() -> rx.Component:
    content = read_markdown_file("content/news.md")
    return default_layout(
        title="News 📰",
        components=[
            rx.markdown(
                content,
                **MARKDOWN_PARAMS,  # type: ignore
            ),
        ],
    )
