import reflex as rx

from divingavran.layouts.default import default_layout

def games() -> rx.Component:
    return default_layout(
        title="Games",
        components=[
        ],
    )
