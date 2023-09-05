import reflex as rx
import requests
import random


class MyState(rx.State):
    quote = ''
    author = ''

    def get_qoute(self):
        url = 'https://type.fit/api/quotes'
        res = requests.get(url)
        data = res.json()
        rand_num = random.randrange(0, len(data))
        self.quote = data[rand_num]['text']
        self.author = data[rand_num]['author']


def header():
    return rx.responsive_grid(
        rx.center(
            rx.box(
                rx.heading('I am Hamzah', size='xl'),
                rx.heading('I am a Pythn Developmenter', size='sm'),
                rx.button('Click Hier', margin_top='2rem', on_click=MyState.get_qoute),
                qoute()
            )
        ),
        rx.center(
            rx.image(src='/i.jpg')
        ),
        columns=[1, 2]

    )


def qoute():
    return rx.box(
        rx.text(MyState.quote, as_='b'),
        rx.text(MyState.author)
    )
