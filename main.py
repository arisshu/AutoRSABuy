#import robinhood as r
import os
import fennel as f
import robinhood as r
import public as p
import firstradeutil as ft
import color as clrs
import helper as utils
from dotenv import load_dotenv

load_dotenv()
os.system("")
os.system('cls')
#r.login("username", "password")
#r.viewHolding()
ROBIN = False
ROBINROTH = False
ROBINIRA = False
FENNEL = False
PUBLIC1 = False
PUBLIC2 = False
FIRSTRADE = False
#print(clrs.c.GREEN)

print("\n==============  FENNEL =================")
if os.getenv("FENNELEMAIL") != "":
    #os.system('cls')
    print("Logging in Fennel...")
    try:
        f.loginSession(os.getenv("FENNELEMAIL"))
        print(f"{clrs.c.GREEN}! Logged in Funnel{clrs.c.END}")
        FENNEL = True
    except:
        print(f"{clrs.c.RED} INVALID credential or INVALID verification code, skipping... {clrs.c.END}")
        pass
else:
    print("No Fennel credential detected, skipping....")
    pass

print("\n============= ROBINHOOD ================")
if (os.getenv("ROBINHOODEMAIL") and os.getenv("ROBINHOODPASSWORD")) != "":
    print("Logging in Robinhood...")
    try:
        r.loginRH(os.getenv("ROBINHOODEMAIL"),os.getenv("ROBINHOODPASSWORD"))
        print(f"{clrs.c.GREEN}! Logged in Robinhood{clrs.c.END}")
        ROBIN = True
    except:
        print(f"{clrs.c.RED} INVALID credential, skipping...{clrs.c.END} ")
        pass
    if (os.getenv("ROBINROTH") != ""): ROBINROTH = True
    if (os.getenv("ROBINIRA") != ""): ROBINIRA = True
else:
    print("No Robinhood credential detected, skipping....")

print("\n============= PUBLIC ================")
if (os.getenv("PUBLIC1_EMAIL") and os.getenv("PUBLIC1_PASS")) != "":
    print("Logging in Public 1...")
    try:
        p.loginSession(os.getenv("PUBLIC1_EMAIL"),os.getenv("PUBLIC1_PASS"))
        #print(os.getenv("PUBLIC1_EMAIL"))
        print(f"{clrs.c.GREEN}! Logged in Public 1{clrs.c.END}")
        PUBLIC1 = True
    except:
        print(f"{clrs.c.RED} INVALID credential, skipping...{clrs.c.END} ")
        pass
else:
    print("No Public 2 credential detected, skipping....")

if (os.getenv("PUBLIC2_EMAIL") and os.getenv("PUBLIC2_PASS")) != "":
    print("Logging in Public 2...")
    
    try:
        p.loginSession(os.getenv("PUBLIC2_EMAIL"),os.getenv("PUBLIC2_PASS"), True)
        print(f"{clrs.c.GREEN}! Logged in Public 2{clrs.c.END}")
        PUBLIC2 = True
    except:
        print(f"{clrs.c.RED} INVALID credential, skipping...{clrs.c.END} ")
        pass
else:
    print("No Public 2 credential detected, skipping....")
    
print("\n==============  FIRSTRADE =================")
if (os.getenv("FIRSTRADEUSER") and os.getenv("FIRSTRADEPASSWORD")) != "":
    #os.system('cls')
    print("Logging in Firstrade...")
    try:
        ft.loginSession(os.getenv("FIRSTRADEUSER"),os.getenv("FIRSTRADEPASSWORD"),os.getenv("FIRSTRADEPIN"))
        print(f"{clrs.c.GREEN}! Logged in Firstrade{clrs.c.END}")
        FIRSTRADE = True
    except:
        print(f"{clrs.c.RED} INVALID credential or INVALID Pin, skipping...{clrs.c.END} ")
        pass
else:
    print("No Firstrade credential detected, skipping....")
    pass

x = None
while (True):
    print(f"{clrs.c.YELLOW}\n\n---------------------------")
    x = int(input(f"(1) Get Position (ALL BROKERAGE) \n(2) Buy Order \n(3) Sell Order \n(Other Key) Exit\n{clrs.c.END}"))
    if x == 1:
        os.system('cls')
        if (FENNEL):
            f.getHolding()
        if (ROBIN):
        #    r.getPosition(os.getenv("ROBINROTH"))
            r.getPosition(os.getenv("ROBINROTH"), os.getenv("ROBINIRA"))
        #    r.getPosition(os.getenv("ROBINROTH"))
        if (PUBLIC1):
            p.getHolding()
        if (PUBLIC2):
            p.getHolding(True)
        if (FIRSTRADE):
            ft.getHolding()
    elif x == 2:
        os.system('cls')
        ticker = input("Ticker name: ")
        if (utils.YFgetStockPrice(ticker) != -1):
            print(f"Current Price: {clrs.c.BLINK2}{round(utils.YFgetStockPrice(ticker),4)}{clrs.c.END}")
        else:
            continue
        limit = float(input("Limit offset price (Put 0 for market price): "))
        if (limit == 0): print(f"{clrs.c.RED}WARNING! Some broker do not allow market order for stock price below $1 !{clrs.c.END}")
        if (FENNEL):
            f.createOrder("buy", ticker)
        if (ROBIN):
            print("[ROBINHOOD] INDIVIDUAL Account:")
            r.rhPlaceOrder("buy",ticker)
            if (ROBINROTH):
                print("[ROBINHOOD] ROTH IRA Account:")
                r.rhPlaceOrder("buy",ticker, os.getenv("ROBINROTH"))
            if (ROBINIRA):
                print("[ROBINHOOD] TRADITIONAL IRA Account:")
                r.rhPlaceOrder("buy",ticker, os.getenv("ROBINIRA"))
            #if (ROBINIRA):
            #    r.rhBuyMarket(ticker, ROBINIRA)
            r.switchValidation()
        if (PUBLIC1):
            print("[PUBLIC 1] PUBLIC INDIVIDUAL ACCOUNT")
            p.placeOrder("buy", ticker)
        if (PUBLIC2):
            print("[PUBLIC 2] PUBLIC INDIVIDUAL ACCOUNT")
            p.placeOrder("buy", ticker, True)
        if (FIRSTRADE):
            ft.buyOrder(ticker,limit)
    elif x == 3:
        os.system('cls')
        ticker = input("Ticker name: ")
        #offset = float(input("Limit Price: "))
        if (FENNEL):
            f.createOrder("sell", ticker)
        if (ROBIN):
            print("[ROBINHOOD] INDIVIDUAL Account:")
            r.rhPlaceOrder("sell", ticker)
            if (ROBINROTH):
                print("[ROBINHOOD] ROTH IRA Account:")
                r.rhPlaceOrder("sell",ticker, os.getenv("ROBINROTH"))
            if (ROBINIRA):
                print("[ROBINHOOD] TRADITIONAL IRA Account:")
                r.rhPlaceOrder("sell",ticker, os.getenv("ROBINIRA"))
        if (PUBLIC1):
            print("[PUBLIC 1] PUBLIC INDIVIDUAL ACCOUNT")
            p.placeOrder("sell", ticker)
        if (PUBLIC2):
            print("[PUBLIC 2] PUBLIC INDIVIDUAL ACCOUNT")
            p.placeOrder("sell", ticker, True)
        if (FIRSTRADE):
            #print("[FIRSTRADE] FIRSTRADE Accounts")
            ft.sellOrder(ticker)


    else:
        os.system("pause")
        exit()