import reflex as rx

from divingavran.components.footer import footer
from divingavran.constants import FONT_COLOR, LINK_FONT_COLOR


def body(components: list[rx.Component], **kwargs) -> rx.Component:
    return rx.flex(
        *components,
        direction="column",
        justify_content="flex-start",
        align_items="center",
        max_width="100svw",
        min_height="100svh",
        **kwargs,
    )


def main(components: list[rx.Component], **kwargs) -> rx.Component:
    return rx.flex(
        *components,
        gap="1.0em",
        direction="column",
        justify_content="center",
        align_items="center",
        width="100%",
        height="100%",
        max_width="1280px",
        **kwargs,
    )


def _navigation_item(text: str, href: str) -> rx.Component:
    return rx.link(
        text,
        href=href,
        color=rx.cond(rx.State.router.page.path == href, LINK_FONT_COLOR, FONT_COLOR),
        text_decoration=rx.cond(rx.State.router.page.path == href, "underline", "none"),
    )


def navigation_bar() -> rx.Component:
    return rx.flex(
        _navigation_item(text="Home", href="/"),
        _navigation_item(text="Games", href="/games"),
        _navigation_item(text="Apps", href="/apps"),
        _navigation_item(text="Music", href="/music"),
        # _navigation_item(text="TIL", href="/til"),
        _navigation_item(text="About", href="/about"),
        direction="row",
        justify_content="center",
        align_items="center",
        gap="1.0em",
    )


def header(**kwargs) -> rx.Component:
    return rx.flex(
        rx.link(
            rx.heading("Divin Gavran", size="8", margin="1.0em 0.0em 0.25em 0.0em"),
            href="/",
            color=FONT_COLOR,
            text_decoration="none",
        ),
        direction="column",
        justify_content="center",
        align_items="center",
        gap="1.0em",
        **kwargs,
    )


def default_layout(
    title: str, components: list[rx.Component], **kwargs
) -> rx.Component:
    return body(
        [
            main(
                [
                    header(),
                    navigation_bar(),
                    rx.heading(
                        title,
                        size="6",
                        margin_top="0.5em",
                        padding="0.0em",
                    ),
                    *components,
                    footer(),
                ]
            )
        ]
    )
