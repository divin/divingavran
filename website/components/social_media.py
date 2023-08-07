from typing import Any

import reflex as rx


def social_media(configuration: dict, **props: Any) -> rx.Component:
    social_media_accounts = configuration["social-media"]
    social_media_accounts = [
        rx.link(
            rx.html(f"<i class='{account['icon']}'></i>"),
            href=account["url"],
            is_external=True,
        )
        for account in social_media_accounts
    ]
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
