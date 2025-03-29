import reflex as rx

from divingavran.pages import home, privacy, imprint, about, music, games, apps, blog

style = {
    "color": "#eeeeee",
    "font_size": "1.0em",
    "font_family": "Lato",
    "font_weight": "400",
    #"a": {
    #    "color": "#eeeeee",
    #},
    "a:hover": {"color": "#2e6960"},
    "background_color": "#0a0c0b",
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

app = rx.App(
    theme=theme,
    style=style,
    head_components=[
        rx.el.script('<script defer src="https://cyber-earwig.pikapod.net/script.js" data-website-id="b20f5d59-9995-4687-be19-dee4c854b25a"></script>')
    ],
    stylesheets=stylesheets,
)

app.add_page(home, title="Divin Gavran", route="/")
app.add_page(blog, title="Blog | Divin Gavran", route="/blog")
app.add_page(about, title="About | Divin Gavran", route="/about")
app.add_page(games, title="Games | Divin Gavran", route="/games")
app.add_page(music, title="Music | Divin Gavran", route="/music")
app.add_page(apps, title="Apps | Divin Gavran", route="/apps")
app.add_page(privacy, title="Privacy | Divin Gavran", route="/privacy")
app.add_page(imprint, title="Imprint | Divin Gavran", route="/imprint")
