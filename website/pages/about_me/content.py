from typing import Any

import reflex as rx

def _skills()

def _cv_event(event: dict) -> rx.Component:
    return rx.accordion_item(
        rx.accordion_button(
            rx.flex(
                rx.html(f"<i class='{event['icon']}'></i>"),
                rx.text(f"{event['from']} - {event['to']}:"),
                event["name"],
                direction="row",
                gap="0.5rem",
            ),
            rx.accordion_icon(),
        ),
        rx.accordion_panel(
            rx.box(
                rx.markdown(event["description"]),
                padding="1.0rem",
            )
        ),
        border="0",
    )


def _cv(cv_events: list) -> rx.Component:
    return rx.flex(
        rx.text("What I've achieved so far:"),
        rx.accordion(
            *[_cv_event(event) for event in cv_events],
            allow_multiple=False,
            allow_toggle=True,
            width="100%",
        ),
        direction="column",
        gap="1.0rem",
    )


def content(cv_events: list, **props: Any) -> rx.Component:
    return rx.flex(
        _cv(cv_events),
        direction="column",
        line_height="1.5rem",  # for text 1.3 to 1.5 time the text size
        letter_spacing="0.025rem",  # for text not negative
        **props,
    )
