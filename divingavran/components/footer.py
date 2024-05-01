from typing import Any

import reflex as rx

from divingavran.utilities import read_yaml

from .site_end import site_end
from .social_media import social_media


def footer(**props: Any) -> rx.Component:
    config = read_yaml("config.yaml")
    accounts = config["accounts"]
    return rx.center(
        rx.flex(
            social_media(accounts=accounts),
            site_end(font_size="0.85em"),
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
