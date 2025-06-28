import reflex as rx

from divingavran.components.card import card
from divingavran.constants import MARKDOWN_PARAMS
from divingavran.layouts.default import default_layout
from divingavran.utilities import read_markdown_file, read_yaml


def apps() -> rx.Component:
    """Renders the apps page.

    Reads markdown content for the page description and configuration
    data for app cards from YAML. It then constructs the page layout
    using the default layout, including the markdown content and
    a list of app cards.

    Returns
    -------
    rx.Component
        The Reflex component representing the apps page.
    """
    content = read_markdown_file("content/apps.md")
    config = read_yaml("config.yaml")
    apps = [card(**app_config) for app_config in config["apps"]]
    return default_layout(
        title="Apps 📱",
        components=[
            rx.markdown(
                content,
                **MARKDOWN_PARAMS,  # type: ignore
            ),
            rx.flex(
                *apps,
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
