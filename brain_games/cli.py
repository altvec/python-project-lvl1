# -*- coding: utf-8 -*-

"""CLI functions."""

import prompt


def run():
    """Request the name of the user and return a greeting."""
    username = prompt.string('May I have your name? ')
    greeting = 'Hello, {username}!'.format(username=username)
    return greeting
