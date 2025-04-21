import os

import reflex as rx

from divingavran.constants import BACKGROUND_COLOR, FONT_COLOR, LINK_FONT_COLOR
from divingavran.pages import about, apps, error, games, home, music, news

style = {
    "color": FONT_COLOR,
    "font_size": "1.0em",
    "font_family": "Lato",
    "font_weight": "400",
    "a:hover": {"color": LINK_FONT_COLOR},
    "background_color": BACKGROUND_COLOR,
}

stylesheets = [
    "/css/reset.css",
    "/css/default.css",
    "/css/lato.css",
    "/css/fontawesome.css",
]
theme = rx.theme(
    appearance="dark", has_background=False, radius="medium", accent_color="green"
)

head_components = [
    rx.el.link(rel="apple-touch-icon", sizes="180x180", href="/apple-touch-icon.png"),
    rx.el.link(rel="icon", type="image/png", sizes="32x32", href="/favicon-32x32.png"),
    rx.el.link(rel="icon", type="image/png", sizes="16x16", href="/favicon-16x16.png"),
    rx.el.link(rel="manifest", href="/site.webmanifest"),
]
is_production = str(os.environ.get("IS_PRODUCTION", "False")) == "True"
if is_production:
    head_components.append(
        rx.el.script(
            defer=True,
            src="https://cyber-earwig.pikapod.net/script.js",
            data_website_id="b20f5d59-9995-4687-be19-dee4c854b25a",
        )
    )
else:
    head_components.append(
        rx.el.script(
            defer=True,
            src="https://cyber-earwig.pikapod.net/script.js",
            data_website_id="0d9d1f2b-b6fb-4859-9eab-46ca0602034d",
        )
    )

app = rx.App(
    theme=theme,
    style=style,  # type: ignore
    head_components=head_components,
    stylesheets=stylesheets,
)

app.add_page(home(), title="Divin Gavran", route="/")
app.add_page(error(), title="404 | Divin Gavran", route="/404")
app.add_page(apps(), title="Apps | Divin Gavran", route="/apps")
app.add_page(news(), title="News | Divin Gavran", route="/news")
app.add_page(about(), title="About | Divin Gavran", route="/about")
app.add_page(games(), title="Games | Divin Gavran", route="/games")
app.add_page(music(), title="Music | Divin Gavran", route="/music")
