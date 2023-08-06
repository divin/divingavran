import os

import reflex as rx

from website.components import layout
from website.utilities import read_markdown, read_yaml


def imprint() -> rx.Component:
    """Creates the about page."""
    configuration = read_yaml(os.getcwd() + "/configuration.yaml")
    text = read_markdown(os.getcwd() + "/content/imprint.md")
    content = [
        rx.box(
            rx.markdown(text),
            text_align="left",
            width="clamp(256px, 50%, 1280px)",
            font_size="clamp(1.0rem, 2.0svh, 3.0rem)",
        )
    ]
    return layout(content, configuration)
