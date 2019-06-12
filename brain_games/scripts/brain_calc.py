# -*- coding: utf-8 -*-

"""Brain calc game."""

from brain_games.engine import game_engine
from brain_games.games.brain_calc import make_question

QUESTION = 'What is the result of the expression?'


def main():
    """Run calc game."""
    game_engine(QUESTION, make_question)


if __name__ == '__main__':
    main()
