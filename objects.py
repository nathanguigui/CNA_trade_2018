##
## EPITECH PROJECT, 2019
## trade_2018
## File description:
## model
##

from statistics import pstdev
from compute import compute_slide_mean, compute_expo_moving_av

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

class CandleStat():
    sigma = 0
    moving_average = 0
    bollinger_min = 0
    bollinger_max = 0
    upward_change = 0
    downward_change = 0
    exponential_moving_average_up = 0
    exponential_moving_average_down = 0
    relative_strength_index = 0
    fast_ema = 0
    slow_ema = 0
    macd_speed = 0
    macd_signal = 0
    stochastic = 0
    stochastic_signal = 0
    williams = 0
    enough = False

class InvestmentHistory():
    qte = []
    price = []

class CandleList():
    def __init__(self, pair):
        self.pair = pair
        self.candles = []
        self.stat = []

    def addCandle(self, GAME, arr):
        candle = Candle()
        stat = CandleStat()
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
        self.computeStat(GAME, stat)

    def getCandleCount(self):
        return len(self.candles)

    def getLastCandle(self):
        if len(self.candles) < 1:
            return None
        return self.candles[-1:][0]

    def getLastStat(self):
        if len(self.stat) < 1:
            return None
        return self.stat[-1:][0]

    def computeExpMovAvUp(self, GAME, stat):
        idx = self.getCandleCount() - 2
        prev_stat = self.getLastStat()
        last_stat = stat
        a = 2 / (1 + GAME.n_latest)
        mme = float(last_stat.upward_change * a + prev_stat.exponential_moving_average_up * (1 - a))
        return (mme)

    def computeExpMovAvDown(self, GAME, stat):
        prev_stat = self.getLastStat()
        last_stat = stat
        a = 2 / (1 + GAME.n_latest)
        mme = float(last_stat.downward_change * a + prev_stat.exponential_moving_average_down * (1 - a))
        return (mme)

    def computeUpDownwardChange(self, GAME, stat):
        idx = self.getCandleCount() - 2
        last = self.getLastCandle()
        prev = self.candles[idx]
        if last.close_val > prev.close_val:
            stat.upward_change = last.close_val - prev.close_val
            stat.downward_change = 0
        elif last.close_val < prev.close_val:
            stat.upward_change = 0
            stat.downward_change = prev.close_val - last.close_val
        else:
            stat.upward_change = 0
            stat.downward_change = 0

    def computeBollinger(self, GAME, stat):
        arr = []
        for candle in self.candles[-GAME.n_latest:]:
            arr.append(candle.close_val)
        stat.sigma = pstdev(arr)
        stat.moving_average = compute_slide_mean(arr, GAME.n_latest)
        stat.bollinger_max = stat.moving_average + (GAME.bollinger_coef * stat.sigma)
        stat.bollinger_min = stat.moving_average - (GAME.bollinger_coef * stat.sigma)

    def computeRSI(self, GAME, stat):
        stat.exponential_moving_average_up = self.computeExpMovAvUp(GAME, stat)
        stat.exponential_moving_average_down = self.computeExpMovAvDown(GAME, stat)
        stat.relative_strength_index = stat.exponential_moving_average_up / (stat.exponential_moving_average_up + abs(stat.exponential_moving_average_down)) * 100

    def computeMACD(self, GAME, stat):
        prev_stat = self.getLastStat()
        last_candle = self.getLastCandle()
        stat.slow_ema = compute_expo_moving_av(last_candle.close_val, GAME.MACD_period[0], prev_stat.slow_ema, self.getCandleCount())
        stat.fast_ema = compute_expo_moving_av(last_candle.close_val, GAME.MACD_period[1], prev_stat.fast_ema, self.getCandleCount())
        stat.macd_speed = stat.slow_ema - stat.fast_ema
        stat.macd_signal = compute_expo_moving_av(stat.macd_speed, GAME.MACD_period[2], prev_stat.macd_signal, self.getCandleCount())
    
    def computeStochastic(self, GAME, stat):
        idx = GAME.stochastic_period[0] - 1
        candle_l = self.candles[-GAME.stochastic_period[0]:]
        stat_l = self.stat[-idx:]
        for i, candle in enumerate(candle_l):
            if i == 0:
                min_val = candle.low_val
                max_val = candle.high_val
            else:
                max_val = max(max_val, candle.high_val)
                min_val = min(max_val, candle.low_val)
        stat.stochastic = 100 * ((self.getLastCandle().close_val - min_val) / (max_val - min_val))
        stat_l.append(stat)
        stoch_l = []
        for stat in stat_l:
            stoch_l.append(stat.stochastic)
        stat.stochastic_signal = compute_slide_mean(stoch_l, GAME.stochastic_period[1])

    def computeWilliams(self, GAME, stat):
        candle_l = self.candles[-GAME.williams_period:]
        for i, candle in enumerate(candle_l):
            if i == 0:
                min_p = min(candle.close_val, candle.close_val)
                max_p = max(candle.close_val, candle.close_val)
            else:
                min_p = min(min_p, candle.close_val)
                max_p = max(max_p, candle.close_val)
        stat.williams = 100 * ((max_p - self.getLastCandle().close_val) / max_p - min_p)

    def computeStat(self, GAME, stat):
        if self.getCandleCount() > 1:
            self.computeUpDownwardChange(GAME, stat)
            self.computeMACD(GAME, stat)
        if self.getCandleCount() > GAME.n_latest:
            self.computeBollinger(GAME, stat)
            self.computeRSI(GAME, stat)
            self.computeStochastic(GAME, stat)
            self.computeWilliams(GAME, stat)
        self.stat.append(stat)
    
    def analyzeBollinger(self):
        max_val = self.getLastStat().bollinger_max - self.getLastStat().bollinger_min
        val = self.getLastCandle().close_val - self.getLastStat().bollinger_min
        return (float(val / max_val))

    def analyzeMACD(self):
        idx = self.getCandleCount() - 2
        prev_stat = self.stat[idx]
        last_stat = self.getLastStat()
        prev_signal = prev_stat.macd_speed - prev_stat.macd_signal
        last_signal = last_stat.macd_speed - last_stat.macd_signal
        if (prev_signal >= -10 and last_signal <= 10):
            return "buy"
        if (prev_signal <= 10 and last_signal >= -10):
            return "sell"
        return "pass"

    def makeAction(self, GAME):
        if self.getCandleCount() < GAME.n_latest:
            return "PASS"
        if self.analyzeBollinger() >= 0.75 or self.analyzeBollinger() <= 0.25:
            if self.getLastStat().relative_strength_index <= 30:
                return "BUY"
            if self.getLastStat().relative_strength_index >= 70:
                return "SELL"
        return "PASS"

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

    def __init__(self, *args, **kwargs):
        self.settings = Settings()
        self.btc_eth_candles = CandleList("BTC_ETH")
        self.usdt_eth_candles = CandleList("USDT_ETH")
        self.usdt_btc_candles = CandleList("USDT_BTC")
        self.usdt_btc_history = InvestmentHistory()

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