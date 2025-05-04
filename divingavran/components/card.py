import reflex as rx

from divingavran.constants import FONT_COLOR, LINK_FONT_COLOR


def _card(
    name: str,
    project_url: str,
    image: str,
    width: int | str,
) -> rx.Component:
    """Create a card component for a project.

    Parameters
    ----------
    name : str
        The name of the project.
    project_url : str
        The URL to the project page (e.g., itch.io).
    image : str
        The path or URL to the project image.
    width : int | str
        The maximum width of the card.

    Returns
    -------
    rx.Component
        A Reflex card component displaying the project information.
    """
    return rx.card(
        rx.link(
            rx.flex(
                rx.image(
                    src=image,
                    alt=name,
                    width="100%",
                    height="auto",
                    flex="1 1 90%",
                    border_radius="0.5rem",
                ),
                rx.flex(
                    rx.text(
                        "Download from itch.io",
                        font_size="1.2em",
                        weight="bold",
                        color=FONT_COLOR,
                    ),
                    rx.html(
                        f"<i class='fas fa-download'></i>",
                        font_size="1.2em",
                        weight="bold",
                        color=FONT_COLOR,
                    ),
                    gap="0.5em",
                    align="center",
                    justify="center",
                    direction="row",
                ),
                gap="0.5em",
                direction="column",
            ),
            href=project_url,
            is_external=True,
        ),
        max_width=width,
        border_radius="0.5rem",
    )


def card(name: str, project_url: str, image: str) -> rx.Component:
    """Create a responsive project card component.

    This function generates a project card that adapts its width based on the
    device screen size (mobile vs. tablet/desktop). It utilizes the internal
    `_card` function to render the actual card content with different widths
    for different screen sizes.

    Parameters
    ----------
    name : str
        The name of the project.
    project_url : str
        The URL to the project page (e.g., itch.io).
    image : str
        The path or URL to the project image.

    Returns
    -------
    rx.Component
        A Reflex fragment containing responsive card components, one for
        mobile view and one for tablet/desktop view.
    """
    return rx.fragment(
        rx.mobile_only(
            _card(
                name=name,
                image=image,
                project_url=project_url,
                width="256px",  # "320px",
            ),
        ),
        rx.tablet_and_desktop(
            _card(
                name=name,
                image=image,
                project_url=project_url,
                width="256px",  # "512px",
            ),
        ),
    )
