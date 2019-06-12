# -*- coding: utf-8 -*-

"""Brain prime game functions."""


from brain_games.games.common import generate_number


def is_prime(number):
    """Check if number is prime or not."""
    if number < 2:
        return False
    counter = 2
    while counter <= number // 2:
        if (number % counter == 0):
            return False
        counter += 1
    return True


def make_question():
    """Generate game question."""
    number = generate_number()
    question = 'Question: {number}'.format(number=number)
    answer = 'yes' if is_prime(number) else 'no'
    return (question, answer)
