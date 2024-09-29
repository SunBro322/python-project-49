#!/usr/bin/env python3
from brain_games import pattern_for_games
from brain_games.games import calc


def main():
    pattern_for_games.pattern(calc.calculate)


if __name__ == 'main':
    main()
