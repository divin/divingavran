import os
from typing import Any

import reflex as rx

def content(greeting: str, about_me: str, **props: Any) -> rx.Component:
    return rx.flex(
        rx.text(
            greeting,
            font_weight="900",
            line_height="1.3rem",  # for heading 1.1 to 1.3 time the text size
            letter_spacing="-0.025rem",  # for heading negative
        ),
        rx.markdown(about_me),
        direction="column",
        line_height="1.5rem",  # for text 1.3 to 1.5 time the text size
        letter_spacing="0.025rem",  # for text not negative
        **props,
    )
