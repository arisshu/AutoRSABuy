from firstrade import account, order, symbols
from firstrade.order import get_orders
import src.color as clrs

acctDATA = None
loginStatus = None
PREFIX = "[FIRSTRADE] "

def loginSession(username, password, pin):
    global acctDATA
    global loginStatus
    loginStatus = account.FTSession(
        username=username,
        password=password,
        pin=pin
    )
    acctDATA = account.FTAccountData(loginStatus)

#Helper function of getting quote
def getQuotePrice(ticker):
    return symbols.SymbolQuote(loginStatus, ticker).last

def getHolding():
    # Local variable to hold account numbers to avoid accessing multiple times
    account_numbers = acctDATA.account_numbers
    securities_held = acctDATA.securities_held
    print("")
    # Iterate over account numbers
    for x in account_numbers:
        print(f"{clrs.c.VIOLET}{PREFIX} Account ID: {x}{clrs.c.END}")

        # Get positions for the account (assuming this call is necessary for each account)
        position = acctDATA.get_positions(account=x)

        # Iterate over securities held
        for y, details in securities_held.items():
            # Fetch quote for the security
            quote = symbols.SymbolQuote(loginStatus, y)

            # Print details
            print(f"{y} x {details['quantity']} \t\tCurrent Price: {quote.last}")

    #print(accList)

def buyOrder(ticker,offset):
    account_numbers = acctDATA.account_numbers

    for x in account_numbers:
        #print(x,"Proceeding buying")
        orderStatus = order.Order(loginStatus)
        orderStatus.place_order(
            x,
            symbol=ticker,
            price_type=order.PriceType.LIMIT,
            price=getQuotePrice(ticker)+offset,
            order_type=order.OrderType.BUY,
            quantity=1,
            duration=order.Duration.DAY,
            dry_run=False,
        )
        print(f"{clrs.c.SELECTED}{PREFIX} Order placed. Limit @ {orderStatus.order_confirmation['Est. Commission']} CHECK APP CONFIRMATION!{clrs.c.END}")

def sellOrder(ticker):
    account_numbers = acctDATA.account_numbers

    for x in account_numbers:
        #print(x)
        orderStatus = order.Order(loginStatus)
        orderStatus.place_order(
            x,
            symbol=ticker,
            price_type=order.PriceType.MARKET,
            order_type=order.OrderType.SELL,
            quantity=1,
            duration=order.Duration.DAY,
            dry_run=False,
        )
        print(f"{clrs.c.SELECTED}{PREFIX} Order placed. Sell @ {orderStatus.order_confirmation['Est. Commission']} CHECK APP CONFIRMATION!{clrs.c.END}")