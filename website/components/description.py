from typing import Any

import reflex as rx


def description(text: str, **props: Any) -> rx.Component:
    return rx.center(
        rx.markdown(
            text,
        ),
        # Font
        font_weight="400",
        font_size="clamp(1.0rem, 3.0svh, 5.0rem)",
        # Size
        padding="1.0rem",
        width="clamp(256px, 80%, 640px)",
        height="clamp(64px, 20%, 320px)",
        **props,
    )
