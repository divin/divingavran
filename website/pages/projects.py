import os
from typing import Any

import reflex as rx

from website.utilities import read_yaml, sort_projects
from website.components import description, heading, layout, project_card


def my_projects(configuration: dict, **props: Any) -> rx.Component:
    """Creates a latest projects component."""
    projects = [project_card(project) for project in sort_projects(configuration["projects-list"])]
    return rx.flex(
        *projects,
        direction="row",
        gap="1.0rem",
        wrap="wrap",
        align_items="center",
        justify="center",
        width="clamp(256px, 80%, 1280px)",
        **props,
    )

def projects() -> rx.Component:
    """Creates the projects  page."""
    configuration = read_yaml(os.getcwd() + "/configuration.yaml")
    text = configuration["projects"]["description"]
    content = [
        heading(
            content=[
                rx.text(configuration["projects"]["greeting"]),
            ],
            flex="0 1 30%",
        ),
        description(
            text=text, text_align="center", flex="1 1 10%"
        ),
        my_projects(configuration=configuration),
    ]
    return layout(content, configuration)
