import reflex as rx

from divingavran.constants import FONT_COLOR, MARKDOWN_PARAMS
from divingavran.layouts.default import default_layout
from divingavran.utilities import read_markdown_file


def home() -> rx.Component:
    intro = read_markdown_file("content/home.md")
    news = read_markdown_file("content/news.md", number_of_lines=7)
    return default_layout(
        title="Hi! I'm Divin 🙋",
        components=[
            rx.markdown(intro, **MARKDOWN_PARAMS),  # type: ignore
            rx.link(
                rx.heading("What's new?", size="5"),
                href="/news",
                color=FONT_COLOR,
                text_decoration="none",
            ),
            rx.markdown(
                news,
                **MARKDOWN_PARAMS,  # type: ignore
            ),
        ],
    )
