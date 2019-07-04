# -*- coding: utf-8 -*-

"""Brain progression game functions."""

from random import choice, randint

DESCRIPTION = 'What number is missing in the progression?'


def make_progression():
    """Generate arithemtic progression."""
    initial_number = randint(1, 100)
    delta = randint(1, 25)
    length = 10
    maximum_number = (delta * length) + initial_number
    prog = [str(num) for num in range(initial_number, maximum_number, delta)]
    return prog


def make_question():
    """Generate game question."""
    prog = make_progression()
    secret = choice(prog)
    progression = ' '.join(['..' if num == secret else num for num in prog])
    question = 'Question: {progression}'.format(progression=progression)
    return (question, secret)
