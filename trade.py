##
## EPITECH PROJECT, 2019
## trade_2018
## File description:
## trade
##

import sys

from objects import Trade

from settings import get_settings
from candle import get_candle, update_stacks
from action import make_action

def get_commands(GAME, av):
    if len(av) < 3:
        return
    if av[0] == "action":
        return make_action(GAME, av)
    if av[0] == "update" and av[1] == "game" and av[2] == "next_candles":
        return get_candle(GAME, av)
    if av[0] == "update" and av[1] == "game" and av[2] == "stacks":
        return update_stacks(GAME, av)

def my_bot():
    GAME = Trade()
    while True:
        try:
            line = input()
        except(KeyboardInterrupt, EOFError):
            break
        av = line.split(' ')
        if GAME.settings.full is False:
            get_settings(GAME, av)
        else:
            get_commands(GAME, av)