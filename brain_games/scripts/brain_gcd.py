#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Brain gcd game."""

from brain_games.engine import run
from brain_games.games import brain_gcd


def main():
    """Run even game."""
    run(brain_gcd)


if __name__ == '__main__':
    main()
