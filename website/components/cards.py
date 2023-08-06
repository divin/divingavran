from typing import Any

import reflex as rx


def project_card(project: dict, **props: Any) -> rx.Component:
    return rx.link(
        rx.image(
            src=project["image"],
            width="100%",
            max_width="384px",
            flex="1 1 auto",
            border_radius="1.0rem",
        ),
        href=project["href"],
        flex="0 1 auto",
        is_external=True,
        **props,
    )
