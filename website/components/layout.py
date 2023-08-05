from typing import Any

import reflex as rx

from .footer import footer
from .navigation import navigation


def layout(content: list[rx.Component], configuration: dict, **props) -> rx.Component:
    max_width = configuration["website"]["max_width"]
    return rx.flex(
        rx.flex(
            navigation(configuration),
            rx.flex(
                *content,
                footer(configuration, font_size="clamp(1.5rem, 4.0svh, 8.0rem)"),
                # Flex
                gap="1.0rem",
                direction="column",
                justify="flex-start",
                align_items="center",
                # Size
                width="100%",
                min_height="100%",
                max_width=max_width,
            ),
            # Flex
            justify="center",
            direction="column",
            align_items="center",
            # Size
            width="100%",
            height="100%",
            max_width=max_width,
            margin_top="12.5svh",
        ),
        # Flex
        direction="column",
        justify="flex-start",
        align_items="center",
        # Size
        max_width="100svw",
        min_height="100svh",
    )
