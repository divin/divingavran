import reflex as rx

from divingavran.layouts.default import default_layout

def home() -> rx.Component:
    return default_layout(
        title="Hi. I'm Divin.",
        components=[],
    )
