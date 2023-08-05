import reflex as rx


def test() -> rx.Component:
    return rx.flex(
        rx.flex(
            # Navigation
            rx.center(
                rx.flex(
                    rx.text("Home"),
                    rx.text("About"),
                    rx.text("Projects"),
                    rx.text("Contact"),
                    # Size
                    width="clamp(576px, 75%, 640px)",
                    height="clamp(32px, 50%, 256px)",
                    # width="clamp(100svw, 100%, 80lvw)",
                    max_width="1280px",
                    # Flex
                    gap="1.0rem",
                    justify="space-evenly",
                    align_items="center",
                    padding="1.0rem",
                    # Background
                    border_radius="256px",
                    backdrop_filter="blur(16px)",
                    background_color="rgba(255, 200, 0, 0.5)",
                    # Font
                    font_size="clamp(16px, 2.5svh, 256px)",
                ),
                # Position
                top="0.0",
                # left="0.0",
                # right="0.0",
                margin="0.0",
                padding="0.0",
                z_index="5",
                position="fixed",
                # Size
                width="100svw",
                height="12.5svh",
            ),
            # Content
            rx.flex(
                rx.center(
                    "Heading",
                    font_size="clamp(2.5rem, 6.0svh, 16.0rem)",
                    flex="0 1 30%",
                    background_color="red",
                ),
                rx.center(
                    "Description",
                    font_size="clamp(1.5rem, 3.0svh, 16.0rem)",
                    flex="0 1 10%",
                    background_color="red",
                ),
                rx.center(
                    "Social Media",
                    font_size="clamp(1.0rem, 2.5svh, 8.0rem)",
                    flex="0 1 5%",
                    background_color="red",
                ),
                rx.flex(
                    rx.center(
                        "Box 1",
                        flex="1 0 clamp(128px, 45%, 256px)",
                        background_color="blue",
                    ),
                    rx.center(
                        "Box 2",
                        flex="1 0 clamp(128px, 45%, 256px)",
                        background_color="blue",
                    ),
                    rx.center(
                        "Box 3",
                        flex="1 0 clamp(128px, 45%, 256px)",
                        background_color="blue",
                    ),
                    rx.center(
                        "Box 4",
                        flex="1 0 clamp(128px, 45%, 256px)",
                        background_color="blue",
                    ),
                    gap="1.0rem",
                    padding="1.0rem",
                    wrap="wrap",
                    flex="1 1 auto",
                    background_color="red",
                ),
                rx.center("Footer", flex="0 1 10%", background_color="red"),
                # Flex
                gap="0.5rem",
                direction="column",
                justify="flex-start",
                # Size
                width="100%",
                min_height="100%",
                max_width="1280px",
                # Background
                background_color="green",
            ),
            direction="column",
            justify="center",
            align_items="center",
            margin_top="12.5svh",
            width="100svw",
            height="100svh",
            max_width="1280px",
            background_color="blue",
        ),
        # Flex
        direction="column",
        justify="flex-start",
        align_items="center",
        # Size
        max_width="100svw",
        min_height="100svh",
    )
