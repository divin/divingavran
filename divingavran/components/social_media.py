from typing import Any

import reflex as rx

from divingavran.constants import FONT_COLOR


def account(name: str, icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.html(f"<i class='{icon}'></i>"),
        href=href,
        color=FONT_COLOR,
        is_external=True,
        font_size="2.0em",
    )


def social_media(accounts: list[dict[str, str]], **props: Any) -> rx.Component:
    social_media_accounts = [account(**account_info) for account_info in accounts]
    return rx.center(
        rx.flex(
            *social_media_accounts,
            gap="1.0rem",
            direction="row",
            justify="center",
        ),
        # Flex
        flex="0 1 5%",
        **props,
    )
