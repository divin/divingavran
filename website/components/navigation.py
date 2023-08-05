from typing import Any

import reflex as rx


def navigation(configuration: dict, **props: Any) -> rx.Component:
    links = [
        rx.link(link["title"], href=link["href"])
        for link in configuration["navigation"]
    ]
    return rx.center(
        rx.flex(
            *links,
            # Size
            max_width="1280px",
            width="clamp(288px, 80%, 640px)",
            height="clamp(32px, 50%, 256px)",
            # Flex
            gap="1.0rem",
            padding="1.0rem",
            align_items="center",
            justify="space-evenly",
            # Background
            border_radius="256px",
            backdrop_filter="blur(16px)",
            background_color="rgba(255, 255, 255, 0.15)",
            # Font
            font_weight="600",
            font_size="clamp(16px, 2.5svh, 256px)",
            **props,
        ),
        # Position
        top="0.0",
        z_index="5",
        margin="0.0",
        padding="0.0",
        position="fixed",
        # Size
        width="100svw",
        height="12.5svh",
        **props,
    )
