# -*- coding: utf-8 -*-

"""Brain even game."""

import sys

import prompt

from brain_games.brain_even import check_answer, generate_number
from brain_games.cli import run

NUMBER_OF_ROUNDS = 3


def game(user_name):
    """Game main logic."""
    correct_answers = 0
    while correct_answers < NUMBER_OF_ROUNDS:
        number = generate_number()
        print('Question: {number}'.format(number=number))
        user_answer = prompt.string('Your answer: ')
        is_right, message = check_answer(user_answer, number)
        print(message)
        if not is_right:
            print("Let's try again, {user_name}!".format(user_name=user_name))
            sys.exit()
        correct_answers += 1
    print('Congratulations, {user_name}!'.format(user_name=user_name))


def main():
    """Run game."""
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".', end='\n\n')
    greeting = run()
    print(greeting, end='\n\n')
    user_name = greeting.split(',')[1].strip()[:-1]
    game(user_name)


if __name__ == '__main__':
    main()
