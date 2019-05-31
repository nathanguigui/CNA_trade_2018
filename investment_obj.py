##
## EPITECH PROJECT, 2019
## trade_2018
## File description:
## investment_obj
##

class Investment():
    qte = 0.0
    price = 0.0
    idx = 0

class InvestmentHistory():
    def __init__(self, pair):
        self.pair = pair
        self.history = []

    def getStokastik(self, current_price):
        stok = 0
        for investment in self.history:
            stok += (investment.qte * (current_price - investment.price))
        return stok

    def addInvestment(self, GAME):
        investment = Investment()
        investment.idx = GAME.usdt_btc_candles.getCandleCount() - 1
        investment.price = GAME.usdt_btc_candles.getLastCandle().close_val
        investment.qte = GAME.countMaxPlacement("USDT", investment.price, 1)
        self.history.append(investment)
        act = "buy USDT_BTC " + str(investment.qte)
        GAME.current_action.append(act)

    def getMoney(self, GAME):
        if self.getStokastik(GAME.usdt_btc_candles.getLastCandle().close_val) <= 15:
            return
        act = "sell USDT_BTC " + str(GAME.BTC)
        GAME.current_action.append(act)