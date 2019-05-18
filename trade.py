#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## trade_2018
## File description:
## trade
##

import sys
from model import Settings, Trade, Candle

def set_candle_format(GAME):
    arr = GAME.settings.candle_txt.split(',')
    for idx, key in enumerate(arr):
        if key == "pair":
            GAME.settings.candle_format.pair_idx = idx
            GAME.settings.candle_format.count += 1
        if key == "date":
            GAME.settings.candle_format.date_idx = idx
            GAME.settings.candle_format.count += 1
        if key == "high":
            GAME.settings.candle_format.high_idx = idx
            GAME.settings.candle_format.count += 1
        if key == "low":
            GAME.settings.candle_format.low_idx = idx
            GAME.settings.candle_format.count += 1
        if key == "open":
            GAME.settings.candle_format.open_idx = idx
            GAME.settings.candle_format.count += 1
        if key == "close":
            GAME.settings.candle_format.close_idx = idx
            GAME.settings.candle_format.count += 1
        if key == "volume":
            GAME.settings.candle_format.volume_idx = idx
            GAME.settings.candle_format.count += 1

def get_settings(GAME, av):
    if (len(av) != 3 ) or (av[0] != "settings"):
        return print("invalid settings")
    if av[1] == "timebank":
        try:
            GAME.settings.timebank = int(av[2])
            GAME.settings.count += 1
        except ValueError:
            return print("invalid settings")
    if av[1] == "time_per_move":
        try:
            GAME.settings.time_per_move = int(av[2])
            GAME.settings.count += 1
        except ValueError:
            return print("invalid settings")
    if av[1] == "player_names":
        try:
            if len(GAME.settings.player_names) == 0:
                GAME.settings.count += 1
            GAME.settings.player_names.append(str(av[2]))
        except ValueError:
            return print("invalid settings")
    if av[1] == "your_bot":
        try:
            GAME.settings.your_bot = str(av[2])
            GAME.settings.count += 1
        except ValueError:
            return print("invalid settings")
    if av[1] == "candle_interval":
        try:
            GAME.settings.candle_interval = int(av[2])
            GAME.settings.count += 1
        except ValueError:
            return print("invalid settings")
    if av[1] == "candles_total":
        try:
            GAME.settings.candles_total = int(av[2])
            GAME.settings.count += 1
        except ValueError:
            return print("invalid settings")
    if av[1] == "candles_given":
        try:
            GAME.settings.candles_given = int(av[2])
            GAME.settings.count += 1
        except ValueError:
            return print("invalid settings")
    if av[1] == "initial_stack":
        try:
            GAME.settings.initial_stack = int(av[2])
            GAME.settings.count += 1
        except ValueError:
            return print("invalid settings")
    if av[1] == "candle_format":
        try:
            GAME.settings.candle_txt = str(av[2])
            GAME.settings.count += 1
            set_candle_format(GAME)
        except ValueError:
            return
    if GAME.settings.count == 9:
        GAME.settings.full = True
        print("Settings full")

def get_candle(GAME, av):
    if len(av) < 4:
        return
    candles = av[3].split(';')
    for candle in candles:
        arr = candle.split(',')
        if arr[GAME.settings.candle_format.pair_idx] == "BTC_ETH":
            GAME.btc_eth_candles.addCandle(GAME, arr)
        if arr[GAME.settings.candle_format.pair_idx] == "USDT_ETH":
            GAME.usdt_eth_candles.addCandle(GAME, arr)
        if arr[GAME.settings.candle_format.pair_idx] == "USDT_BTC":
            GAME.usdt_btc_candles.addCandle(GAME, arr)

def update_stacks(GAME, av):
    if len(av) < 4:
        return
    stacks = av[3].split(',')
    for stack in stacks:
        arr = stack.split(':')
        if arr[0] == "BTC":
            try:
                GAME.BTC = float(arr[1])
            except ValueError:
                pass
        if arr[0] == "ETH":
            try:
                GAME.ETH = float(arr[1])
            except ValueError:
                pass
        if arr[0] == "USDT":
            try:
                GAME.USDT = float(arr[1])
            except ValueError:
                pass

def make_action(GAME, av):
    print("pass")

def get_commands(GAME, av):
    if len(av) < 3:
        return
    if av[0] == "action":
        return make_action(GAME, av)
    if av[0] == "update" and av[1] == "game" and av[2] == "next_candles":
        return get_candle(GAME, av)
    if av[0] == "update" and av[1] == "game" and av[2] == "stacks":
        return update_stacks(GAME, av)

def main():
    GAME = Trade()
    while True:
        try:
            line = input()
        except(KeyboardInterrupt, EOFError):
            sys.exit(84)
        av = line.split(' ')
        if GAME.settings.full is False:
            get_settings(GAME, av)
        else:
            get_commands(GAME, av)

if __name__ == "__main__":
    main()