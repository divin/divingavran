"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx

from rxconfig import config

from .pages import about_me, index


class State(rx.State):
    """The app state."""

    pass


style = {
    "font_size": "1.0rem",
    "font_weight": "400",
    "font_family": "Lato",
    "font_style": "normal",
}

stylesheets = ["css/default.css"]

app = rx.App(state=State, style=style, stylesheets=stylesheets)

app.add_page(component=index, route="/", title="Divin Gavran")

app.add_page(component=about_me, route="/about-me", title="Divin Gavran | About Me")

app.add_page(
    component=rx.heading("Imprint"), route="/imprint", title="Divin Gavran | Imprint"
)

app.add_page(
    component=rx.heading("Privacy Policy"),
    route="/privacy",
    title="Divin Gavran | Privacy Policy",
)

app.compile()
