import reflex as rx

from divingavran.constants import MARKDOWN_PARAMS
from divingavran.layouts.default import default_layout
from divingavran.utilities import read_markdown_file


def news() -> rx.Component:
    """Renders the news page.

    Reads content from the 'content/news.md' markdown file and displays it
    within the default application layout.

    Returns
    -------
    rx.Component
        A Reflex component representing the news page, including the
        rendered markdown content.
    """
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
