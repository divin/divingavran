import reflex as rx


def _embed_itchio(
    name: str,
    embed_id: str,
    project_url: str,
    width: int | str,
    height: int | str = "167",
    foreground_color: str = "#eeeeee",
    background_color: str = "#222222",
    link_color: str = "#2e6960",
    border_color: str = "#222222",
    **kwargs,
) -> rx.Component:
    background_color = background_color.replace("#", "")
    foreground_color = foreground_color.replace("#", "")
    link_color = link_color.replace("#", "")
    border_color = border_color.replace("#", "")
    src = f"https://itch.io/embed/{embed_id}?linkback=true&amp;bg_color={background_color}&amp;fg_color={foreground_color}&amp;link_color={link_color}&amp;border_color={border_color}"

    return rx.html(
        f"""
        <iframe frameborder="0" src="{src}" width="{width}" height="{height}">
            <a href="{project_url}">{name} by Divin Gavran</a>
        </iframe>
    """,
        **kwargs,
    )


def game(name: str, embed_id: str, project_url: str) -> rx.Component:
    return rx.fragment(
        rx.mobile_only(
            _embed_itchio(
                name=name,
                embed_id=embed_id,
                project_url=project_url,
                width="208",
            ),
        ),
        rx.tablet_and_desktop(
            _embed_itchio(
                name=name,
                embed_id=embed_id,
                project_url=project_url,
                width="552",
            ),
        ),
    )
