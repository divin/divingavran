import reflex as rx

from divingavran.components.game import game
from divingavran.layouts.default import default_layout
from divingavran.utilities import read_yaml


def about_me() -> rx.Component:
    return rx.markdown(
        """
        I'm a **data scientist** with a **background in physics** who loves programming and unraveling insights from complex data.

        When I'm not crunching numbers, you'll find me immersed in game development, which blends my passions for art, music, and programming.
        I'm currently focused on creating games for the [Playdate Console](https://play.date).
        **Feel free to check out my [GitHub](https://github.com/divin), my [Itch.io](https://divingavran.itch.io) page or my latest games below!**
        """,
        text_align="justify",
        max_width="640px",
        margin="1.0rem",
        style={
            "a": {
                "text-decoration": "underline",
            },
        },
    )


def index() -> rx.Component:
    config = read_yaml("config.yaml")
    games = config["games"]
    components = [
        about_me(),
        *[game(**game_info) for game_info in games],
    ]
    return default_layout(
        title="Hi. I'm Divin.",
        components=components,
    )
