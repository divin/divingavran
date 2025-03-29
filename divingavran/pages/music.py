import reflex as rx

from divingavran.layouts.default import default_layout

def music() -> rx.Component:
    return default_layout(
        title="Music",
        components=[],
    )
