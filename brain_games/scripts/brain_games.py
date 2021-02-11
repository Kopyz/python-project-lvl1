#!/usr/bin/env python3

"""Brain game console script."""


from brain_games.cli import welcome_user


def main():
    """Print greeting with name from console input."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
