import reflex as rx

from divingavran.components.footer import footer


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
        gap="1.0rem",
        direction="column",
        justify_content="center",
        align_items="center",
        width="100%",
        height="100%",
        max_width="1280px",
        **kwargs,
    )


def header(title: str, **kwargs) -> rx.Component:
    return rx.flex(
        rx.link(rx.image(src="/logo.png", width="128px", height="auto"), href="/"),
        rx.heading(title, size="8"),
        direction="column",
        justify_content="center",
        align_items="center",
        gap="1.0rem",
        **kwargs,
    )


def default_layout(
    title: str, components: list[rx.Component], **kwargs
) -> rx.Component:
    return body(
        [
            main(
                [
                    header(title=title),
                    *components,
                    footer(),
                ]
            )
        ]
    )
