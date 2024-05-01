import reflex as rx

from divingavran.layouts.default import default_layout
from divingavran.utilities import read_markdown_file


def privacy() -> rx.Component:
    content = read_markdown_file("content/privacy.md")
    markdown = rx.markdown(
        content, text_align="justify", max_width="640px", margin="1.0rem"
    )
    return default_layout(title="Privacy", components=[markdown])
