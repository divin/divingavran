import reflex as rx

from divingavran.layouts.default import default_layout

def about() -> rx.Component:
    return default_layout(
        title="About",
        components=[
        ],
    )
