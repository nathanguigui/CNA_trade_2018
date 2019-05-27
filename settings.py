##
## EPITECH PROJECT, 2019
## trade_2018
## File description:
## settings
##

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
        GAME.USDT = GAME.settings.initial_stack