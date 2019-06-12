# -*- coding: utf-8 -*-

"""Brain gcd game functions."""

from brain_games.engine import generate_number


def make_question():
    """Generate game question."""
    num1 = generate_number()
    num2 = generate_number()
    question = 'Question: {num1} {num2}'.format(num1=num1, num2=num2)
    answer = gcd(num1, num2)
    return (question, str(answer))


def gcd(num1, num2):
    """Return GCD of two numbers."""
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)
