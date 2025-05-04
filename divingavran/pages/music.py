import urllib.parse

import reflex as rx

from divingavran.constants import MARKDOWN_PARAMS
from divingavran.layouts.default import default_layout
from divingavran.utilities import read_markdown_file, read_yaml


def embedded_player(url: str, size: int = 160) -> rx.Component:
    """Generate an embedded Bandcamp player component.

    Parameters
    ----------
    url : str
        The URL of the Bandcamp track or album.
    size : int, optional
        The size (width and height) of the player in pixels, by default 170.

    Returns
    -------
    rx.Component
        A Reflex HTML component containing the iframe for the Bandcamp player.
    """
    encoded_url = urllib.parse.quote(url, safe="")
    return rx.html(
        f'<iframe style="border: 0; width: {size}px; height: {size}px;" src="https://bandcamp.com/EmbeddedPlayer/url={encoded_url}/size=large/bgcol=ffffff/linkcol=2ebd35/minimal=true/transparent=true/" seamless></iframe>'
    )


def music() -> rx.Component:
    """Create the music page component.

    Reads music content from a markdown file and configuration from YAML,
    then generates the page layout including embedded Bandcamp players.

    Returns
    -------
    rx.Component
        The Reflex component representing the entire music page.
    """
    content = read_markdown_file("content/music.md")
    config = read_yaml("config.yaml")
    divin_urls = config["divin"]
    karasu_urls = config["karasu"]
    return default_layout(
        title="Music 🎶",
        components=[
            rx.markdown(
                content,
                **MARKDOWN_PARAMS,  # type: ignore
            ),
            rx.heading("Divin", size="5"),
            rx.flex(
                *[embedded_player(**url) for url in divin_urls],
                wrap="wrap",
                gap="1.0em",
                padding="0.5em",
                direction="row",
                align_items="stretch",
                align_content="flex-start",
                justify="center",
                max_width="640px",
            ),
            rx.heading("Karasu-san", size="5"),
            rx.flex(
                *[embedded_player(**url) for url in karasu_urls],
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
