import reflex as rx


def navbar():
    return rx.flex(
        rx.box(
            rx.link(
                rx.icon(
                    tag="lock",),
                href='/',
            )
        ),
        rx.center(
            rx.menu(
                rx.menu_button('MENU'),
                rx.menu_list(
                    rx.menu_item(rx.link('About', href='/about')),
                    rx.menu_item('Posts')),

            )
        ),
        justify_content='space-between'

    )
