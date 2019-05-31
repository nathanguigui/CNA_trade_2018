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

def make_etherum_action(GAME):
    if GAME.usdt_eth_candles.makeAction(GAME) == "BUY" and GAME.countMaxPlacement("USDT", GAME.usdt_eth_candles.getLastCandle().close_val, 0.5) != 0:
        GAME.usdt_eth_investment.addInvestment(GAME)
    elif GAME.usdt_eth_candles.makeAction(GAME) == "SELL" and GAME.ETH != 0:
        GAME.usdt_eth_investment.getMoney(GAME)

def make_crypto_swap(GAME):
    if GAME.BTC != 0:   #on a BTC
        if GAME.usdt_btc_candles.makeAction(GAME) != "SELL": #pas moment vente
            if GAME.btc_eth_candles.makeAction(GAME) == "BUY": #moment achat ETH
                GAME.bth_eth_investment.swapCrypto(GAME, "buy")
    elif GAME.ETH != 0:
        if GAME.usdt_eth_candles.makeAction(GAME) != "SELL":
            if GAME.btc_eth_candles.makeAction(GAME) == "SELL":
                GAME.bth_eth_investment.swapCrypto(GAME, "sell")


def make_action(GAME, av):
    # make_crypto_swap(GAME)
    # make_bitcoin_action(GAME)
    make_etherum_action(GAME)
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