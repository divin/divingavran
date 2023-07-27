import os
from typing import Any

import reflex as rx

from utilities import get_link, read_yaml


def _social_media_account(account: dict) -> rx.Component:
    return get_link(
        title=rx.html(f"<i class='{account['icon']}'></i>"), href=account["url"]
    )


def _get_social_media_accounts() -> list[rx.Component]:
    configuration = read_yaml(os.getcwd() + "/configuration.yaml")
    social_media_accounts = configuration["social-media"]
    return [_social_media_account(account=account) for account in social_media_accounts]


def social_media_accounts(**props: Any) -> rx.Component:
    social_media_accounts: list[rx.Component] = _get_social_media_accounts()
    return rx.flex(
        *social_media_accounts,
        gap="1.0rem",
        direction="row",
        font_size="1.25rem",
        **props,
    )
