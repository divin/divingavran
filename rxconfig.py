import reflex as rx


class WebsiteConfig(rx.Config):
    pass


config = WebsiteConfig(
    app_name="website",
    env=rx.Env.DEV,
)
