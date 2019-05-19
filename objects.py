##
## EPITECH PROJECT, 2019
## trade_2018
## File description:
## model
##

class CandleFormat():
    pair_idx = 0
    date_idx = 0
    high_idx = 0
    low_idx = 0
    open_idx = 0
    close_idx = 0
    volume_idx = 0
    count = 0

class Candle():
    date_val = 0
    high_val = 0
    low_val = 0
    open_val = 0
    close_val = 0
    volume_val = 0

class CandleList():
    def __init__(self, pair):
        self.pair = pair
        self.candles = []

    def getCandleCount(self):
        return len(self.candles)

    def isGrowing(self):
        if len(self.candles) < 1:
            return None
        if self.candles[-1:].open > self.candles[-1:].close:
            return False
        return True
    
    def addCandle(self, GAME, arr):
        candle = Candle()
        for idx, value in enumerate(arr):
            if GAME.settings.candle_format.date_idx == idx:
                try:
                    candle.date_val = float(value)
                except ValueError:
                    return
            if GAME.settings.candle_format.high_idx == idx:
                try:
                    candle.high_val = float(value)
                except ValueError:
                    return
            if GAME.settings.candle_format.low_idx == idx:
                try:
                    candle.low_val = float(value)
                except ValueError:
                    return
            if GAME.settings.candle_format.open_idx == idx:
                try:
                    candle.open_val = float(value)
                except ValueError:
                    return
            if GAME.settings.candle_format.close_idx == idx:
                try:
                    candle.close_val = float(value)
                except ValueError:
                    return
            if GAME.settings.candle_format.volume_idx == idx:
                try:
                    candle.volume_val = float(value)
                except ValueError:
                    return
        self.candles.append(candle)

class Settings():
    def __init__(self, *args, **kwargs):
        self.candle_format = CandleFormat()
    timebank = 0
    time_per_move = 0
    player_names = []
    your_bot = None
    candle_interval = 0
    candles_total = 0
    candles_given = 0
    initial_stack = 0
    transaction_fee_percent = 0.2
    candle_txt = ""
    count = 0;
    full = False

class Trade():
    BTC = 0.0
    ETH = 0.0
    USDT = 0.0
    def __init__(self, *args, **kwargs):
        self.settings = Settings()
        self.btc_eth_candles = CandleList("BTC_ETH")
        self.usdt_eth_candles = CandleList("USDT_ETH")
        self.usdt_btc_candles = CandleList("USDT_BTC")