import reflex as rx


class WebsiteConfig(rx.Config):
    pass


config = WebsiteConfig(
    app_name="website",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)
