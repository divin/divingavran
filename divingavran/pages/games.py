import reflex as rx

from divingavran.components.card import card
from divingavran.constants import MARKDOWN_PARAMS
from divingavran.layouts.default import default_layout
from divingavran.utilities import read_markdown_file, read_yaml


def games() -> rx.Component:
    """Renders the games page.

    Reads markdown content for the page description and configuration
    data for game cards from YAML. It then constructs the page layout
    using the default layout, including the markdown content and
    a list of game cards.

    Returns
    -------
    rx.Component
        The Reflex component representing the games page.
    """
    content = read_markdown_file("content/games.md")
    config = read_yaml("config.yaml")
    games = [card(**game_config) for game_config in config["games"]]
    return default_layout(
        title="Games 🎮",
        components=[
            rx.markdown(
                content,
                **MARKDOWN_PARAMS,  # type: ignore
            ),
            rx.flex(
                *games,
                wrap="wrap",
                gap="1.0em",
                padding="0.5em",
                direction="row",
                align_items="stretch",
                align_content="flex-start",
                justify="center",
                max_width="640px",
            ),
        ],
    )
