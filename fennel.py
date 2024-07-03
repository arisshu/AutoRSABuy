from fennel_invest_api import Fennel
import color as clrs

PREFIX="[FENNEL]"

f = Fennel()
def loginSession(user):
    loginStatus = f.login(
        email=user,
    )
    #print(loginStatus)
    
def getHolding():
    account_ids = f.get_account_ids()
    print(f"{clrs.c.CBLUE2}{PREFIX} You have {len(account_ids)} account(s){clrs.c.END}")
    for account_id in account_ids:
        print(f'{clrs.c.CBLUE2}Account ID: {account_id}{clrs.c.END}')
        positions = f.get_stock_holdings(account_id)
        #print(positions)
        for position in positions:
            #print(position)
            #print("\nAccount: "+ position['isin'])
            print(position['security']['ticker'] +" x " +  position['investment']['ownedShares'] + "\t\tCurrent Price: "+position['security']['currentStockPrice'])
        #print("")

def positionExistCheck(ticker, account):
    #account_ids = f.get_account_ids()
    #for account_id in accountList:
        #print(f'Checking existing')
    positions = f.get_stock_holdings(account)
    for position in positions:
        if ticker in position['security']['ticker']:
            #print("positionExistCheck position existed check")
            return True

def createOrder(side, ticker):
    #ticker = input("Ticker name: ")
    try:
        validation = f.get_stock_quote(ticker)
    except:
        validation = None

    if side == "buy":
        if validation is None:
            print(f"{clrs.c.RED}{PREFIX} That ticker does not exist, try again{clrs.c.END}")
        else:
            print(f"{PREFIX} Found "+validation['security']['ticker']+" priced @ "+validation['security']['currentStockPrice'])
            x = input(f"{PREFIX} Proceed to buy on Fennel (Y/n)? ")
            #print(x)
            if x.lower() == "y":
                print("Proceeding buying on Fennel")
                account_ids = f.get_account_ids()
                for account_id in account_ids:
                    #print(account_id)
                    if (positionExistCheck(ticker, account_id)):
                        print(f"{clrs.c.RED}{PREFIX} Bruh, you already have 1 share of {ticker}, skipping...{clrs.c.END}")
                    else:
                        #print("Proceed placing order")
                        order = f.place_order( 
                            account_id=account_id,
                            ticker=ticker,
                            quantity=1,
                            side=side, # Must be "buy" or "sell"
                            price="market" # Only market orders are supported for now
                        )
                        print(f'{clrs.c.SELECTED}{PREFIX}Order placed. Check App confirmation!{clrs.c.END}')
            else:
                pass

    if side == "sell":
        account_ids = f.get_account_ids()
        for account_id in account_ids:
            print(account_id)

            order = f.place_order( 
                account_id=account_id,
                ticker=ticker,
                quantity=1,
                side=side, # Must be "buy" or "sell"
                price="market" # Only market orders are supported for now
            )
            print(order)

