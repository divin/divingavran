import reflex as rx

from divingavran.pages.imprint import imprint
from divingavran.pages.index import index
from divingavran.pages.privacy import privacy

style = {
    "color": "#eeeeee",
    "font_size": "1.0rem",
    "font_family": "Lato",
    "font_weight": "400",
    "a": {
        "color": "#eeeeee",
    },
    "a:hover": {"color": "#2e6960"},
}

stylesheets = ["css/default.css"]
theme = rx.theme(
    appearance="dark", has_background=True, radius="medium", accent_color="green"
)

app = rx.App(
    theme=theme,
    style=style,
    stylesheets=stylesheets,
)

app.add_page(index, title="Divin Gavran", route="/")
app.add_page(privacy, title="Privacy | Divin Gavran", route="/privacy")
app.add_page(imprint, title="Imprint | Divin Gavran", route="/imprint")
