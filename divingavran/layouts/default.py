import reflex as rx

from divingavran.components.footer import footer
from divingavran.constants import FONT_COLOR, LINK_FONT_COLOR


def body(components: list[rx.Component], **kwargs) -> rx.Component:
    """Creates the main body container for the page.

    This component acts as the root flex container, setting the overall
    page direction, alignment, and minimum height.

    Parameters
    ----------
    components : list[rx.Component]
        A list of Reflex components to render within the body.
    **kwargs
        Additional keyword arguments to pass to the `rx.flex` component.

    Returns
    -------
    rx.Component
        A Reflex flex component representing the page body.
    """
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
    """Creates the main content area within the body.

    This component centers the primary content horizontally and vertically,
    setting a maximum width.

    Parameters
    ----------
    components : list[rx.Component]
        A list of Reflex components to render within the main content area.
    **kwargs
        Additional keyword arguments to pass to the `rx.flex` component.

    Returns
    -------
    rx.Component
        A Reflex flex component representing the main content area.
    """
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
    """Creates a single navigation link item.

    This is a helper function for `navigation_bar`. It creates a link
    that changes color and text decoration based on the current page route.

    Parameters
    ----------
    text : str
        The display text for the navigation link.
    href : str
        The URL path the link should navigate to.

    Returns
    -------
    rx.Component
        A Reflex link component representing a navigation item.
    """
    return rx.link(
        text,
        href=href,
        color=rx.cond(rx.State.router.page.path == href, LINK_FONT_COLOR, FONT_COLOR),
        text_decoration=rx.cond(rx.State.router.page.path == href, "underline", "none"),
    )


def navigation_bar() -> rx.Component:
    """Creates the main navigation bar component.

    Contains links to different sections of the website. Uses the
    `_navigation_item` helper function to create individual links.

    Returns
    -------
    rx.Component
        A Reflex flex component representing the navigation bar.
    """
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
    """Creates the header component with the site title.

    Displays the main site heading ("Divin Gavran") as a link to the homepage.

    Parameters
    ----------
    **kwargs
        Additional keyword arguments to pass to the `rx.flex` component.

    Returns
    -------
    rx.Component
        A Reflex flex component representing the site header.
    """
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
    """Provides a default page layout structure.

    Combines the header, navigation bar, page title, main content components,
    and footer into a standard page structure using the `body` and `main`
    layout components.

    Parameters
    ----------
    title : str
        The title to display for the specific page.
    components : list[rx.Component]
        A list of Reflex components representing the main content of the page.
    **kwargs
        Additional keyword arguments passed down to the underlying layout components.

    Returns
    -------
    rx.Component
        A Reflex component representing the complete page layout.
    """
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
                ],
                **kwargs,
            )
        ],
    )
