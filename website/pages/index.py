import os
from typing import Any

import reflex as rx

from website.utilities import read_yaml, sort_projects
from website.components import description, heading, layout, social_media, project_card

def latest_projects(configuration: dict, **props: Any) -> rx.Component:
    """Creates a latest projects component."""
    projects = [project_card(project) for project in sort_projects(configuration["projects-list"])][:4]
    return rx.flex(
        heading("Latest Projects", flex="1 1 100%"),
        *projects,
        direction="row",
        gap="1.0rem",
        wrap="wrap",
        align_items="center",
        justify="center",
        width="clamp(256px, 80%, 1280px)",
        **props,
    )

def index() -> rx.Component:
    """Creates the index page."""
    configuration = read_yaml(os.getcwd() + "/configuration.yaml")
    text = configuration["home"]["description"]
    content = [
        heading(
            content=[
                rx.text(configuration["home"]["greeting"]),
                rx.text(configuration["home"]["subgreeting"]),
            ],
            flex="0 1 30%",
        ),
        description(
            text=text, text_align="center", flex="1 1 10%"
        ),
        social_media(configuration=configuration, font_size="clamp(1.5rem, 4.0svh, 8.0rem)"),
        latest_projects(configuration=configuration),
    ]
    return layout(content, configuration)
