import reflex as rx

from divingavran.layouts.default import default_layout

def apps() -> rx.Component:
    return default_layout(
        title="Apps",
        components=[
        ],
    )
