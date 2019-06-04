# -*- coding: utf-8 -*-

"""Program entry point."""

from brain_games.cli import run


def main():
    """Run program."""
    print('Welcome to the Brain Games!')
    greeting = run()
    print(greeting)


if __name__ == '__main__':
    main()
