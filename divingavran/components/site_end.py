from datetime import date
from typing import Any

import reflex as rx

from divingavran.constants import FONT_COLOR


def site_end(seperator: str = "|", **props: Any) -> rx.Component:
    return rx.center(
        rx.flex(
            rx.link(
                f"{date.today().strftime('%Y')} © Divin", href="/", color=FONT_COLOR
            ),
            gap="0.5em",
            direction="row",
            justify="center",
            align_items="center",
            align_content="stretch",
        ),
        **props,
    )
