import os
from typing import Any

import reflex as rx

from website.utilities import read_yaml, sort_projects
from website.components import description, heading, layout, project_card

def contact() -> rx.Component:
    """Creates the contact  page."""
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
        rx.html(
            "<form name='contact' netlify><input type='email' name='email' placeholder='Your E-Mail' required><textarea name='message' placeholder='Your Message' required></textarea><button type='submit'>Send</button></form>"
        ),
    ]
    return layout(content, configuration)
