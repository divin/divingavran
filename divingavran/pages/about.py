import httpx
import reflex as rx

from divingavran.constants import MARKDOWN_PARAMS
from divingavran.layouts.default import default_layout
from divingavran.utilities import read_markdown_file


class FormState(rx.State):
    """State management for the contact form."""

    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle the form submission asynchronously.

        This method takes the form data, adds the access key for web3forms,
        and sends the data via a POST request. It then displays a success
        or error toast message based on the response status.

        Parameters
        ----------
        form_data : dict
            A dictionary containing the data submitted through the contact form.
            Expected keys are 'name', 'email', and 'message'.

        Returns
        -------
        rx.event.EventSpec
            A Reflex event spec that triggers either a success or error toast message
            in the frontend.
        """
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
    """Create the contact form component.

    This function builds a Reflex form component containing input fields for
    name, email, and message, along with a submit button. The form submission
    is handled by the `FormState.handle_submit` method.

    Returns
    -------
    rx.Component
        A Reflex form component for user contact.
    """
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
    """Create the About page component.

    This function reads the content for the about page from a markdown file,
    renders it using `rx.markdown`, includes the contact form component,
    and wraps everything in the default layout.

    Returns
    -------
    rx.Component
        A Reflex component representing the complete About page.
    """
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
