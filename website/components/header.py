from typing import Any

import reflex as rx

from website.constants import GREEN, OFF_WHITE

_logo: rx.Component = rx.box(
    width="2.0rem",
    height="2.0rem",
    display="inline-block",
    background_color=OFF_WHITE,
    mask_size="contain",
    mask_position="center",
    mask_repeat="no-repeat",
    mask_image="url('/images/Logo-Cleaned.png')",
    _hover={"color": GREEN, "cursor": "pointer"},
)


def _heading() -> rx.Component:
    return rx.link(
        rx.heading(
            "Divin Gavran",
            # flex="1 1 auto",
            # text_align="left",
        ),
        href="/",
        _hover={"color": GREEN, "cursor": "pointer"},
    )


def _theme_switcher() -> rx.Component:
    return rx.html(
        "<i class='fas fa-moon'></i>",
        flex="1 1 auto",
        text_align="right",
        _hover={"color": GREEN, "cursor": "pointer"},
    )


def mobile_header(**props: Any) -> rx.Component:
    return rx.mobile_only(
        rx.flex(
            _heading(),
            _theme_switcher(),
            wrap="nowrap",
            direction="row",
            align_items="center",
            justify="space-between",
            align_content="flex-start",
            **props,
        )
    )


def desktop_header(**props: Any) -> rx.Component:
    return rx.tablet_and_desktop(
        rx.flex(
            _heading(),
            _theme_switcher(),
            wrap="nowrap",
            direction="row",
            align_items="center",
            justify="space-between",
            align_content="flex-start",
            **props,
        )
    )
