import reflex as rx
from .components.navbar import navbar
from .components.header import header


def index():
    return rx.container(
        navbar(),
        rx.Divider(),
        header()
    )


def about():
    return rx.container(
        navbar(),
        rx.Divider(),
    )


app = rx.App()
app.add_page(index)
app.add_page(about, route='/about')
app.compile()
