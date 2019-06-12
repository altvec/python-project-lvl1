# -*- coding: utf-8 -*-

"""Brain progression game functions."""

from random import choice, randint


def make_progression():
    """Generate arithemtic progression."""
    initial_number = randint(1, 100)
    delta = randint(1, 25)
    length = 10
    progression = []
    while length:
        initial_number += delta
        progression.append(str(initial_number))
        length -= 1
    return progression


def make_question():
    """Generate game question."""
    prog = make_progression()
    secret = choice(prog)
    progression = ' '.join(['..' if num == secret else num for num in prog])
    question = 'Question: {progression}'.format(progression=progression)
    return (question, secret)
