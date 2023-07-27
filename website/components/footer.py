import os
from datetime import date
from typing import Any

import reflex as rx

from utilities import get_link
from website.constants import GREEN, OFF_WHITE

from .social_media import social_media_accounts


def _site_end(seperator: str = "|", **props: Any) -> rx.Component:
    return rx.flex(
        get_link(title=f"{date.today().strftime('%Y')} © Divin", href="/", **props),
        seperator,
        get_link(title="Imprint", href="/imprint", **props),
        seperator,
        get_link(title="Privacy Policy", href="/privacy", **props),
        gap="0.5rem",
        direction="row",
        font_size="0.75rem",
        align_items="center",
        justify="space-between",
        align_content="stretch",
        **props,
    )


def mobile_footer(**props: Any) -> rx.Component:
    return rx.mobile_only(
        rx.flex(
            social_media_accounts(),
            _site_end(),
            direction="column",
            align_items="center",
            align_content="stretch",
            justify="space-between",
            **props,
        )
    )


def desktop_footer(**props: Any) -> rx.Component:
    return rx.tablet_and_desktop(
        rx.flex(
            social_media_accounts(),
            _site_end(),
            justify="center",
            direction="column",
            align_items="center",
            **props,
        )
    )
