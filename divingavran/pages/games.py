import reflex as rx

from divingavran.components.game import game
from divingavran.constants import MARKDOWN_PARAMS
from divingavran.layouts.default import default_layout
from divingavran.utilities import read_markdown_file, read_yaml


def games() -> rx.Component:
    content = read_markdown_file("content/games.md")
    config = read_yaml("config.yaml")
    games = [game(**game_config) for game_config in config["games"]]
    return default_layout(
        title="Games 🎮",
        components=[
            rx.markdown(
                content,
                **MARKDOWN_PARAMS,  # type: ignore
            ),
            *games,
        ],
    )
