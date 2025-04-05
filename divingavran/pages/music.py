import urllib.parse

import reflex as rx

from divingavran.constants import MARKDOWN_PARAMS
from divingavran.layouts.default import default_layout
from divingavran.utilities import read_markdown_file, read_yaml


def embedded_player(url: str, size: int = 170) -> rx.Component:
    encoded_url = urllib.parse.quote(url, safe="")
    return rx.html(
        f'<iframe style="border: 0; width: {size}px; height: {size}px;" src="https://bandcamp.com/EmbeddedPlayer/url={encoded_url}/size=large/bgcol=ffffff/linkcol=2ebd35/minimal=true/transparent=true/" seamless></iframe>'
    )


def music() -> rx.Component:
    content = read_markdown_file("content/music.md")
    config = read_yaml("config.yaml")
    urls = config["music"]
    return default_layout(
        title="Music 🎶",
        components=[
            rx.markdown(
                content,
                **MARKDOWN_PARAMS,  # type: ignore
            ),
            rx.flex(
                *[embedded_player(**url) for url in urls],
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
