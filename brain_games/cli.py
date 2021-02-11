"""Get username from console input."""


import prompt


def welcome_user():
    """Ask username and print greeting."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
