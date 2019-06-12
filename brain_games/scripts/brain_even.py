# -*- coding: utf-8 -*-

"""Brain even game."""

from brain_games.engine import game_engine
from brain_games.games.brain_even import make_question

QUESTION = 'Answer "yes" if number even otherwise answer "no".'


def main():
    """Run even game."""
    game_engine(QUESTION, make_question)


if __name__ == '__main__':
    main()
