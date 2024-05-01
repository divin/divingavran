from datetime import date
from typing import Any

import reflex as rx


def site_end(seperator: str = "|", **props: Any) -> rx.Component:
    return rx.center(
        rx.flex(
            rx.link(f"{date.today().strftime('%Y')} © Divin", href="/"),
            seperator,
            rx.link("Imprint", href="/imprint"),
            seperator,
            rx.link("Privacy Policy", href="/privacy"),
            gap="0.5em",
            direction="row",
            justify="center",
            align_items="center",
            align_content="stretch",
        ),
        **props,
    )
