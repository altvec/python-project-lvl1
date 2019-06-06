# -*- coding: utf-8 -*-

"""Brain calc game functions."""

from random import choice

from brain_games.games.common import generate_number


def sum_numbers(num1, num2):
    """Sum of two numbers."""
    return num1 + num2


def sub_numbers(num1, num2):
    """Subtract one number from another."""
    return num1 - num2


def mult_numbers(num1, num2):
    """Multiply two numbers."""
    return num1 * num2


operations = {
    '+': sum_numbers,
    '-': sub_numbers,
    '*': mult_numbers,
}


def generate_operation():
    """Generate random operation."""
    return choice(list(operations.keys()))


def correct_answer(num1, operation, num2):
    """Return correct answer."""
    return str(operations[operation](num1, num2))


def make_question():
    """Generate game question."""
    num1 = generate_number()
    num2 = generate_number()
    operation = generate_operation()
    question = 'Question: {n1} {op} {n2}'.format(n1=num1, op=operation, n2=num2)
    answer = correct_answer(num1, operation, num2)
    return (question, answer)
