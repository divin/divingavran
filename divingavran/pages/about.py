import httpx
import reflex as rx

from divingavran.constants import MARKDOWN_PARAMS
from divingavran.layouts.default import default_layout
from divingavran.utilities import read_markdown_file


class FormState(rx.State):
    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        # Use your access key
        form_data["access_key"] = "09574d3b-79f2-46c3-914e-e3fb23f11225"

        # Make the POST request to web3forms
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.web3forms.com/submit",
                data=form_data,
                follow_redirects=True,
            )
            if response.status_code in [200, 201, 301]:
                return rx.toast.success("Message sent successfully!")
            else:
                return rx.toast.error("Failed to send message.")


def contact() -> rx.Component:
    return rx.form(
        rx.flex(
            rx.heading("Contact Me 📧", size="5"),
            rx.input(
                placeholder="Name",
                name="name",
                required=True,
                min_width="204px",
                max_width="640px",
            ),
            rx.input(
                placeholder="Email",
                name="email",
                type="email",
                required=True,
                min_width="204px",
                max_width="640px",
            ),
            rx.text_area(
                placeholder="Message",
                name="message",
                required=True,
                min_width="204px",
                max_width="640px",
            ),
            rx.button("Submit", type="submit"),
            direction="column",
            gap="1em",
            align_items="center",
        ),
        on_submit=FormState.handle_submit,
        reset_on_submit=True,
    )


def about() -> rx.Component:
    content = read_markdown_file("content/about.md")
    return default_layout(
        title="About 🙋",
        components=[
            rx.markdown(
                content,
                **MARKDOWN_PARAMS,  # type: ignore
            ),
            contact(),
        ],
    )
