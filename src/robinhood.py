import robin_stocks.robinhood as r
import src.color as clrs
#import json

PREFIX="[ROBINHOOD]"


def loginRH(email, pwd):
    login = r.login(email, pwd)

#holding = r.build_holdings()

def getPosition(roth=None, ira=None):
    #print(r.load_account_profile(accountNumber))
    holding = r.build_holdings()
    rothHolding = r.get_open_stock_positions(roth)
    iraHolding = r.get_open_stock_positions(ira)

    symbols = [x['symbol'] for x in rothHolding] + [x['symbol'] for x in iraHolding]
    #print(symbols)
    currentPrices = r.get_quotes(symbols)

    print(f"{clrs.c.GREEN}\n{PREFIX} Your Individual brokerage account{clrs.c.END}")
    for key, value in holding.items():
        print(f"{key} x {value['quantity']} \tCurrent Price: {value['price']}")

    if roth is not None:
        print(f"{clrs.c.GREEN}{PREFIX} Your Roth IRA account{clrs.c.END}")
        for x in rothHolding:
            for y in currentPrices:
                if y['symbol'] == x['symbol']:
                    print(f"{x['symbol']} x {x['quantity']} \tCurrent Price: {y['last_trade_price']}")
                    break

    if ira is not None:
        print(f"{clrs.c.GREEN}{PREFIX} Your Traditional IRA account{clrs.c.END}")
        for x in iraHolding:
            for y in currentPrices:
                if y['symbol'] == x['symbol']:
                    print(f"{x['symbol']} x {x['quantity']} \tCurrent Price: {y['last_trade_price']}")
                    break

def validationPrompted(ticker):
    validate = r.get_quotes(ticker)

    if any(x is None for x in validate):
        print(f"{clrs.c.RED}{PREFIX} That ticker does not exist, try again{clrs.c.END}")
        return False
    else:
        for x in validate:
            print(f"{PREFIX} Found {x['symbol']} @ {x['last_trade_price']}")
            user_input = input(f"{PREFIX} Proceed to buy on Robinhood (Y/n)? ")
        if user_input.lower() == "y": return True
        else: return False

def switchValidation():
    global validated
    validated = False

validated = None
def rhPlaceOrder(side, ticker, accountNumber=None):
    global validated, previousTicker
    if (validated == None or validated == False) and side == "buy":
        validated = validationPrompted(ticker)
    #if any(x is None for x in validate):
    #    print(f"{PREFIX} That ticker does not exist, try again")
    #else:
    if side == "buy":
        if validated:
            #for x in validate:
                #print(f"{PREFIX} Found {x['symbol']} @ {x['last_trade_price']}")
                #user_input = input(f"{PREFIX} Proceed to buy on Robinhood (Y/n)? ")
            #if user_input.lower() == "y":
            if accountNumber:
                #print("Proceed buy on ira account")
                if (positionExistCheck(ticker,accountNumber)):
                    print(f"{clrs.c.RED}{PREFIX} Bruh, you already have 1 share of {ticker}, skipping...{clrs.c.END}")
                    pass
                else:
                    #print("Proceed buy on ira account")
                    buyStatus = r.order_buy_market(ticker, 1, accountNumber)

            else:
                #print("Proceed buy on individual account")
                if (positionExistCheck(ticker)):
                    print(f"{clrs.c.RED}{PREFIX} Bruh, you already have 1 share of {ticker}, skipping...{clrs.c.END}")
                    pass
                else:
                    #print("Proceed buy on individual account")
                    buyStatus = r.order_buy_market(ticker, 1)
                
            print(f"{clrs.c.SELECTED}{PREFIX} Order placed. Status: {buyStatus['state'].upper()} CHECK APP CONFIRMATION!{clrs.c.END}")
        else:
            pass
    else:
        if accountNumber:
            try:
                sellStatus = r.order_sell_market(ticker, 1, accountNumber, 'gfd')
                print(f"{PREFIX} Order placed. Status: {sellStatus['state'].upper()} CHECK APP CONFIRMATION")
            except:
                if (sellStatus['detail'] == "Never bought shares in that Instrument."):
                    print(f"{clrs.c.RED}{PREFIX} Insufficent share to sell{clrs.c.END}")
                else:
                    print(f"{clrs.c.RED}{PREFIX} Something wrong can't sell share {sellStatus}{clrs.c.END}")
                pass
                pass
        else:
            try:
                sellStatus = r.order_sell_market(ticker, 1, timeInForce='gfd')
                print(f"{PREFIX} Order placed. Status: {sellStatus['state'].upper()} CHECK APP CONFIRMATION")
            except:
                if (sellStatus['detail'] == "Never bought shares in that Instrument."):
                    print(f"{clrs.c.RED}{PREFIX} Insufficent share to sell{clrs.c.END}")
                else:
                    print(f"{clrs.c.RED}{PREFIX} Something wrong can't sell share {sellStatus}{clrs.c.END}")
                pass
                #print(sellStatus)

def positionExistCheck(ticker, account=None):
    #print("Checking exist stock")
    if account == None:
        holding = r.build_holdings()
        #print(holding)
        for key in holding.items():
            #print(key)
            if (ticker in key):
                return True
        return False
    else:
        holding = r.get_open_stock_positions(account)
        for x in holding:
            if (ticker in x['symbol']):
                return True
        return False
