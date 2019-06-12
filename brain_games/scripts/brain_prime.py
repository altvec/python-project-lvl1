# -*- coding: utf-8 -*-

"""Brain prime game."""

from brain_games.engine import game_engine
from brain_games.games.brain_prime import make_question

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    """Run prime game."""
    game_engine(QUESTION, make_question)


if __name__ == '__main__':
    main()