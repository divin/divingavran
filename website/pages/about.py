import os
from typing import Any

import reflex as rx

from website.utilities import read_yaml
from website.components import description, heading, layout


def hex_to_rgb(hex: str) -> tuple[int, int, int]:
    """Converts a hex color to rgb."""
    hex = hex.lstrip("#")
    return tuple(int(hex[i : i + 2], 16) for i in (0, 2, 4))


def sort_skills(skills: list[dict]) -> list[dict]:
    """Sorts skills by value."""
    return sorted(skills, key=lambda skill: skill["value"], reverse=True)


def skill(name: str, value: int, color: str, **props: Any) -> rx.Component:
    """Creates a skill component."""
    return rx.flex(
        rx.text(name, flex="1 1 50%"),
        rx.progress(
            value=value,
            width="100%",
            color_scheme=color,
            flex="1 1 50%",
            border_radius="0.5em",
        ),
        direction="row",
        align_items="center",
        justify="space-between",
        **props,
    )


def accordion(header: rx.Component, content: rx.Component, **props: Any) -> rx.Component:
    """Creates an accordion component."""
    return rx.accordion(
        rx.accordion_item(
            rx.accordion_button(
                header,
                rx.accordion_icon(),
                font_size="clamp(1.0rem, 3.0svh, 5.0rem)",
            ),
            rx.accordion_panel(
                content,
            ),
            border="none",
        ),
        # Flex
        flex="1 0 auto",
        # Accordion
        allow_toggle=True,
        allow_multiple=False,
        # Size
        padding="1.0rem",
        border_radius="0.5rem",
        width="clamp(256px, 80%, 1280px)",
        **props,
    )

def skills_card(
    header: rx.Component,
    skills: list[rx.Component],
    background_color: str,
    **props: Any,
) -> rx.Component:
    """Creates a skills card component."""
    rgb = hex_to_rgb(background_color)
    content = rx.flex(*skills, direction="column", **props)
    background_color=f"rgba({rgb[0]}, {rgb[1]}, {rgb[2]}, 0.25)"
    return accordion(header=header, content=content, background_color=background_color, **props)


def skills(configuration: dict) -> rx.Component:
    """Creates a skills component."""
    background_color = configuration["website"]["colors"]["accent"]
    tools = [
        skill(tools["name"], tools["value"], "green")
        for tools in sort_skills(configuration["skills"]["tools"])
    ]
    coding = [
        skill(coding["name"], coding["value"], "green")
        for coding in sort_skills(configuration["skills"]["coding"])
    ]
    python = [
        skill(python["name"], python["value"], "green")
        for python in sort_skills(configuration["skills"]["python"])
    ]
    languages = [
        skill(language["name"], language["value"], "green")
        for language in sort_skills(configuration["skills"]["languages"])
    ]
    return rx.flex(
        skills_card(
            header=rx.hstack(rx.html("<i class='fas fa-language'></i>"), rx.text("Languages", font_weight="600")),
            skills=languages,
            background_color=background_color,
        ),
        skills_card(
            header=rx.hstack(rx.html("<i class='fas fa-code'></i>"), rx.text("Coding", font_weight="600")),
            skills=coding,
            background_color=background_color,
        ),
        skills_card(
            header=rx.hstack(rx.html("<i class='fab fa-python'></i>"), rx.text("Python Libraries", font_weight="600")),
            skills=python,
            background_color=background_color,
        ),
        skills_card(
        header=rx.hstack(rx.html("<i class='fas fa-tools'></i>"), rx.text("Tools", font_weight="600")),
            skills=tools,
            background_color=background_color,
        ),
        wrap="wrap",
        gap="1.0rem",
        column="row",
        font_size="clamp(1.0rem, 3.0svh, 5.0rem)",
        width="clamp(256px, 80%, 1280px)",
    )


def background_event(event: dict, background_color: str) -> rx.Component:
    """Creates a cv event component."""
    rgb = hex_to_rgb(background_color)
    return rx.flex(
        rx.flex(
            rx.html(f"<i class='{event['icon']}'></i>"),
            rx.text(event["from"] + " - " + event["to"]),
            gap="1.0rem",
            direction="row",
        ),
        rx.text(event["name"], font_weight="600"),
        rx.markdown(event["description"]),
        gap="0.5rem",
        padding="1.0rem",
        direction="column",
        align_items="left",
        justify="space-between",
        font_size="clamp(0.95rem, 2.5svh, 5.0rem)",
        border_radius="0.5rem",
        width="clamp(192px, 100%, 1280px)",
        background_color=f"rgba({rgb[0]}, {rgb[1]}, {rgb[2]}, 0.125)",
    )


def background(configuration: dict, **props) -> rx.Component:
    """Creates a background component."""
    background_color = configuration["website"]["colors"]["accent"]
    rgb = hex_to_rgb(background_color)
    cv_events = [background_event(event, background_color) for event in configuration["background"]]

    header=rx.hstack(rx.html("<i class='fas fa-trophy'></i>"), rx.text("Background", font_weight="600"))
    content=rx.flex(*cv_events, gap="1.0rem", direction="column", **props)
    background_color=f"rgba({rgb[0]}, {rgb[1]}, {rgb[2]}, 0.25)"
    return accordion(header=header, content=content, background_color=background_color, **props)


def about() -> rx.Component:
    """Creates the about page."""
    configuration = read_yaml(os.getcwd() + "/configuration.yaml")
    content = [
        heading([rx.text(configuration["about"]["greeting"])], flex="0 1 30%"),
        rx.flex(
            rx.image(
                src="images/about.jpg",
                width="100%",
                flex="1 1 auto",
                border_radius="0.5rem",
            ),
            description(
                configuration["about"]["description"],
                text_align="block",
                flex="1 1 50%",
            ),
            wrap="wrap",
            column="row",
            flex="1 1 20%",
            width="clamp(256px, 80%, 1280px)",
        ),
        background(configuration),
        skills(configuration),
    ]
    return layout(content, configuration)
