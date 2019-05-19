##
## EPITECH PROJECT, 2019
## trade_2018
## File description:
## input
##

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