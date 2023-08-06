import os

import reflex as rx

from website.utilities import read_yaml

from .pages import about, imprint, index, privacy, projects
from .states import State

# Get website configuration
configuration = read_yaml(os.getcwd() + "/configuration.yaml")
website_config = configuration["website"]

style = {
    # Links
    "a": {
        "color": website_config["colors"]["text"],
    },
    "a:hover": {
        "color": website_config["colors"]["accent"],
    },
    # Font
    "color": website_config["colors"]["text"],
    "font_size": website_config["font_size"],
    "font_weight": website_config["font_family"],
    "font_family": website_config["font_weight"],
    # Background
    "background_repeat": "repeat-y",
    "background_size": r"10000% 10000%",
    "background": website_config["colors"]["background"],
    "background": "linear-gradient(45deg, #334c3a, #527a53)",  # noqa: F601
    "animation": "gradientFlow 10s ease infinite",
}

stylesheets = ["css/default.css"]

app = rx.App(state=State, style=style, stylesheets=stylesheets)

app.add_page(component=index, route="/", title="Divin Gavran")

app.add_page(component=projects, route="/projects", title="Divin Gavran | Projects")

app.add_page(component=about, route="/about", title="Divin Gavran | About")

app.add_page(component=imprint, route="/imprint", title="Divin Gavran | Imprint")

app.add_page(
    component=privacy,
    route="/privacy",
    title="Divin Gavran | Privacy Policy",
)

app.compile()
