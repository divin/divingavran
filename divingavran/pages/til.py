import reflex as rx

from divingavran.layouts.default import default_layout


def til() -> rx.Component:
    return default_layout(
        title="Today I Learned",
        components=[],
    )
