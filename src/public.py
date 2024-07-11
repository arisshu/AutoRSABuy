from public_invest_api import Public
import src.color as clrs
#import logging as log


PREFIX = "[PUBLIC]"

p1 = Public(filename="public_credentials1.pkl")
p2 = Public(filename="public_credentials2.pkl")
def loginSession(user, password, type=False):
    objectAcct = None
    if (type): objectAcct=p2
    else: objectAcct=p1

    loginStatus = objectAcct.login(
        username=user,
        password=password,
        wait_for_2fa=True
    )

def getHolding(type=False):
    objectAcct = None
    if (type): objectAcct=p2
    else: objectAcct=p1

    positions = objectAcct.get_positions()
    if (len(positions) == 0):
        print(f"No stock owned under this account")

    if (type): print(f"{clrs.c.BEIGE}{PREFIX} Your 2nd Public Acct position{clrs.c.END}")
    else: print(f"\n{clrs.c.BEIGE}{PREFIX} Your 1st Public Acct position{clrs.c.END}")
    for x in positions:
        print(f"{x['instrument']['symbol']} x {x['quantity']} \t\tCurrent Price: {x['previousClose']['previousClose']}")


def placeOrder(side, ticker, type=False):
    objectAcct = None
    if (type): objectAcct=p2
    else: objectAcct=p1

    try:
        validation = objectAcct.get_order_quote(ticker)
        #print(validation)
    except:
        validation = None
        #print(validation)

    if (side=='buy'):
        if (positionExistCheck(ticker,objectAcct)):
            print(f"{clrs.c.RED}{PREFIX} Bruh, you already have 1 share of {ticker}, skipping...{clrs.c.END}")
            pass
        else:
            if validation is None:
                print(f"{clrs.c.YELLOW}{PREFIX} That ticker does not exist, try again{clrs.c.END}")
                #log.warning(f"{PREFIX} {validation} at Buy Procedure")
                pass
            else:
                #print(validation)
                #print(f"{PREFIX} Found {validation['symbol']} @ {validation['last']}")
                #x = input(f"{PREFIX} Proceed to buy (Y/n)? ")
                #if x.lower() == "y":
                    #print("Proceed buying on Public")
                order = objectAcct.place_order(
                    symbol=ticker,
                    quantity=1,
                    side=side,
                    order_type='MARKET',
                    time_in_force='DAY',
                    tip=0,
                )
                print(f"{clrs.c.SELECTED}{PREFIX} Order placed. STATUS: {order['status']} CHECK APP CONFIRMATION{clrs.c.END}")
    else:
        #print("Proceed selling procedure")
        try:
            order = objectAcct.place_order(
                symbol=ticker,
                quantity=1,
                side=side,
                order_type='MARKET',
                time_in_force='DAY',
                tip=0,
            )
            print(f"{clrs.c.SELECTED}{PREFIX} Order placed. STATUS: {order['status']} CHECK APP CONFIRMATION{clrs.c.END}")
        except:
            print(f"{clrs.c.RED}{PREFIX} Insufficent share to sell and would result in a short position{clrs.c.END} ")
            pass

def positionExistCheck(ticker, accObj):
    positions = accObj.get_positions()
    for x in positions:
        if (ticker in x['instrument']['symbol']):
            return True
    return False
