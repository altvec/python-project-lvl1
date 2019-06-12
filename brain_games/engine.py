# -*- coding: utf-8 -*-

"""Game engine functions."""

import sys
from random import randint

from brain_games.cli import get_user_answer, get_user_name

NUMBER_OF_ROUNDS = 3


def generate_number():
    """Return random number from range."""
    return randint(1, 100)


def check_answer(user_answer, correct_answer):
    """Check users answer."""
    if user_answer == correct_answer:
        message = 'Correct!'
        return (True, message)
    message = "'{wrong}' is wrong answer ;(. Correct answer was '{correct}'."
    return (False, message.format(wrong=user_answer, correct=correct_answer))


def welcome_user(game_task=None):
    """Welcome user and print task."""
    print('Welcome to the Brain Games!')
    if game_task is None:
        print('')
    else:
        print(game_task, end='\n\n')
    user_name = get_user_name()
    greeting = 'Hello, {user_name}!'.format(user_name=user_name)
    if game_task is None:
        print(greeting)
    else:
        print(greeting, end='\n\n')
    return user_name


def game_engine(game_task, question_and_answer=None):
    """Game engine."""
    user_name = welcome_user(game_task)
    if question_and_answer is None:
        sys.exit()
    correct_answers = 0
    while correct_answers < NUMBER_OF_ROUNDS:
        question, correct_answer = question_and_answer()
        print(question)
        res, msg = check_answer(get_user_answer(), correct_answer)
        if res:
            print(msg)
            correct_answers += 1
        else:
            print(msg)
            print("Let's try again, {user_name}!".format(user_name=user_name))
            sys.exit()
    print('Congratulations, {user_name}!'.format(user_name=user_name))
