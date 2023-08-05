from typing import Any

import reflex as rx


def heading(content: list[rx.Component], **props: Any) -> rx.Component:
    return rx.center(
        rx.flex(
            *content,
            wrap="nowrap",
            direction="column",
            text_align="center",
        ),
        # Font
        font_weight="600",
        font_family="Prociono",
        letter_spacing="-0.112rem",
        font_size="clamp(2.0rem, 6.0svh, 16.0rem)",
        line_height="clamp(3.25rem, 7.8svh, 20.8rem)",
        # Size
        padding="1.0rem",
        width="clamp(10rem, 85%, 1280px)",
        height="clamp(10rem, 40%, 40rem)",
        **props,
    )
