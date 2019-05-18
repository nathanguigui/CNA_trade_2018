##
## EPITECH PROJECT, 2019
## trade_2018
## File description:
## model
##

class CandleFormat():
    pair_idx = None
    date_idx = None
    high_idx = None
    low_idx = None
    open_idx = None
    close_idx = None
    volume_idx = None
    count = 0

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
    transaction_fee_percent = 0.002
    candle_format = ""
    count = 0;
    full = False

class Trade():
    def __init__(self, *args, **kwargs):
        self.settings = Settings()