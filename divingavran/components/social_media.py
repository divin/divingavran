from typing import Any

import reflex as rx

from divingavran.constants import FONT_COLOR


def account(name: str, icon: str, href: str) -> rx.Component:
    """Create a Reflex link component for a social media account.

    Parameters
    ----------
    name : str
        The name of the social media account (currently unused).
    icon : str
        The CSS class string for the icon (e.g., Font Awesome class).
    href : str
        The URL the link should point to.

    Returns
    -------
    rx.Component
        A Reflex link component displaying the icon and linking externally.
    """
    return rx.link(
        rx.html(f"<i class='{icon}'></i>"),
        href=href,
        color=FONT_COLOR,
        is_external=True,
        data_umami_event="external_link_clicked",
        data_umami_event_url=href,
        font_size="2.0em",
    )


def social_media(accounts: list[dict[str, str]], **props: Any) -> rx.Component:
    """Create a Reflex component displaying a row of social media icons.

    Parameters
    ----------
    accounts : list[dict[str, str]]
        A list of dictionaries, where each dictionary contains the 'name',
        'icon', and 'href' for a social media account.
    **props : Any
        Additional keyword arguments to pass to the `rx.center` component.

    Returns
    -------
    rx.Component
        A Reflex center component containing a flex layout of social media icons.
    """
    social_media_accounts = [account(**account_info) for account_info in accounts]
    return rx.center(
        rx.flex(
            *social_media_accounts,
            gap="1.0rem",
            direction="row",
            justify="center",
        ),
        # Flex
        flex="0 1 5%",
        **props,
    )
