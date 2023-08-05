from typing import Any

import reflex as rx

from .site_end import site_end
from .social_media import social_media


def footer(configuration: dict, **props: Any) -> rx.Component:
    return rx.center(
        rx.flex(
            social_media(configuration),
            site_end(font_size="0.5em"),
            justify="center",
            direction="column",
            align_items="center",
            align_content="stretch",
        ),
        gap="0.8em",
        flex="1 1 20%",
        padding="1.0rem",
        **props,
    )
