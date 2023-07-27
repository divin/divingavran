import os
from typing import Any

import reflex as rx

from utilities import read_yaml
from website.components import (
    desktop_footer,
    desktop_header,
    mobile_footer,
    mobile_header,
)
from website.constants import DARK_GREY, OFF_WHITE

from .content import content


def _mobile_view(cv_events: list, **props: Any) -> rx.Component:
    return rx.mobile_only(
        rx.flex(
            mobile_header(height="10svh", padding="1.0rem", **props),
            content(cv_events=cv_events, min_height="78svh", padding="1.0rem", **props),
            mobile_footer(
                height="10svh", padding="1.0rem", margin_bottom="1.0rem", **props
            ),
            direction="column",
            **props,
        ),
        width="100svw",
        height="100svh",
        overflow_x="hidden",
        overflow_y="auto",
    )


def _desktop_view(cv_events: list, **props: Any) -> rx.Component:
    return rx.tablet_and_desktop(
        rx.flex(
            rx.flex(
                desktop_header(height="10vh", padding="1.0rem", **props),
                content(
                    cv_events=cv_events, min_height="78vh", padding="1.0rem", **props
                ),
                desktop_footer(height="10vh", padding="1.0rem", **props),
                direction="column",
                **props,
            ),
            width="100vw",
            height="100vh",
            justify="center",
            overflow_y="auto",
            overflow_x="hidden",
            align_items="center",
            background_color=DARK_GREY,
        )
    )


def about_me() -> rx.Component:
    # Read the configuration file
    configuration = read_yaml(os.getcwd() + "/configuration.yaml")
    website_configuration = configuration["website-configuration"]
    cv_events = configuration["cv-events"]

    return rx.fragment(
        _mobile_view(
            cv_events=cv_events,
            width=website_configuration["mobile"]["width"],
            max_width=website_configuration["mobile"]["max-width"],
            color=OFF_WHITE,
            background_color=DARK_GREY,
        ),
        _desktop_view(
            cv_events=cv_events,
            width=website_configuration["desktop"]["width"],
            max_width=website_configuration["desktop"]["max-width"],
            color=OFF_WHITE,
            background_color=DARK_GREY,
        ),
    )
