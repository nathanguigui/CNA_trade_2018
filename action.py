##
## EPITECH PROJECT, 2019
## trade_2018
## File description:
## action
##

def make_bitcoin_action(GAME):
    if GAME.usdt_btc_candles.makeAction(GAME) == "BUY" and GAME.countMaxPlacement("USDT", GAME.usdt_btc_candles.getLastCandle().close_val, 1) != 0:
        GAME.usdt_btc_investment.addInvestment(GAME)
    elif GAME.usdt_btc_candles.makeAction(GAME) == "SELL" and GAME.BTC != 0:
        GAME.usdt_btc_investment.getMoney(GAME)

def make_action(GAME, av):
    make_bitcoin_action(GAME)
    if len(GAME.current_action) == 0:
        print("pass")
    elif len(GAME.current_action) == 1:
        print(GAME.current_action[0])
    else:
        for idx, action in enumerate(GAME.current_action):
            if idx == len(GAME.current_action) - 1:
                print(action)
            else:
                print(action, end=';')
    GAME.current_action.clear()