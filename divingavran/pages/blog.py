import reflex as rx

from divingavran.layouts.default import default_layout

def blog() -> rx.Component:
    return default_layout(
        title="Blog",
        components=[
        ],
    )
