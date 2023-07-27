import reflex as rx

from website.constants import GREEN


def get_link(title: str | rx.Component, href: str, **props) -> rx.Component:
    return rx.link(
        title, href=href, _hover={"color": GREEN, "cursor": "pointer"}, **props
    )
