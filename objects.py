##
## EPITECH PROJECT, 2019
## trade_2018
## File description:
## model
##

from candle_obj import CandleFormat, CandleList
from investment_obj import InvestmentHistory

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

    n_latest = 20
    stochastic_period = [5, 3]
    bollinger_coef = 1.4
    MACD_period = [12, 26, 9]
    williams_period = 14
    current_action = []

    def __init__(self, *args, **kwargs):
        self.settings = Settings()
        self.btc_eth_candles = CandleList("BTC_ETH")
        self.bth_eth_investment = InvestmentHistory("BTC_ETH")
        self.usdt_eth_candles = CandleList("USDT_ETH")
        self.usdt_eth_investment = InvestmentHistory("USDT_ETH")
        self.usdt_btc_candles = CandleList("USDT_BTC")
        self.usdt_btc_investment = InvestmentHistory("USDT_BTC")

    def countMaxPlacement(self, curr, price, pc):
        USDT = self.USDT * pc
        BTC = self.BTC * pc
        ETH = self.ETH * pc
        if curr == "USDT":
            return float(USDT / price)
        if curr == "ETH":
            return float((ETH / price) - ((ETH / price) * (self.settings.transaction_fee_percent / 100)))
        if curr == "BTC":
            return float((BTC / price) - ((BTC / price) * (self.settings.transaction_fee_percent / 100)))

    def countCashOut(self, curr, price):
        if curr == "USDT":
            return float((self.USDT * price) - ((self.USDT * price) * (self.settings.transaction_fee_percent / 100)))
        if curr == "ETH":
            return float((self.ETH * price) - ((self.ETH * price) * (self.settings.transaction_fee_percent / 100)))
        if curr == "BTC":
            return float((self.BTC * price) - ((self.BTC * price) * (self.settings.transaction_fee_percent / 100)))