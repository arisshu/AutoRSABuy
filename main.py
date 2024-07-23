import os
import time
import survey
import src.fennel as f
import src.robinhood as r
import src.public as p
import src.firstradeutil as ft
import src.color as clrs
import src.helper as utils
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

state = None
with survey.graphics.SpinProgress(prefix = 'Loading... ', suffix = lambda self: state, epilogue = 'Done!') as progress:
    for state in (state, ' Grabbing data...', ' Importing...', ' Handshaking stock exchange...'):
        time.sleep(1.5)

os.system('cls')
if (FENNEL): print(f"{clrs.c.GREEN}✓ Fennel module activated{clrs.c.END}")
else: print(f"{clrs.c.YELLOW}✖ Fennel module disabled{clrs.c.END}")
if (ROBIN): print(f"{clrs.c.GREEN}✓ Robinhood module activated{clrs.c.END}")
else: print(f"{clrs.c.YELLOW}✖ Robinhood module disabled{clrs.c.END}")
if (PUBLIC1 or PUBLIC2): print(f"{clrs.c.GREEN}✓ Public module activated{clrs.c.END}")
else: print(f"{clrs.c.YELLOW}✖ Public module disabled{clrs.c.END}")
if (FIRSTRADE): print(f"{clrs.c.GREEN}✓ Firstrade module activated{clrs.c.END}")
else: print(f"{clrs.c.YELLOW}✖ Firstrade module disabled{clrs.c.END}")


# x = None
# while (x != 0):
#     print(f"{clrs.c.YELLOW}\n\n---------------------------")
#     x = int(input(f"[1] Get Position (ALL BROKERAGE) \n[2] Buy Order \n[3] Sell Order \n[4] Search stock exist on broker (WIP, not working fully)\n[Ctrl+C] Exit\n{clrs.c.END}"))
#     if x == 1:
#         os.system('cls')
#         if (FENNEL):
#             f.getHolding()
#         if (ROBIN):
#         #    r.getPosition(os.getenv("ROBINROTH"))
#             r.getPosition(os.getenv("ROBINROTH"), os.getenv("ROBINIRA"))
#         #    r.getPosition(os.getenv("ROBINROTH"))
#         if (PUBLIC1):
#             p.getHolding()
#         if (PUBLIC2):
#             p.getHolding(True)
#         if (FIRSTRADE):
#             ft.getHolding()
#     elif x == 2:
#         os.system('cls')
#         ticker = input("Ticker name: ")
#         if (utils.YFgetStockPrice(ticker) != -1):
#             print(f"Current Price: {clrs.c.BLINK2}{round(utils.YFgetStockPrice(ticker),4)}{clrs.c.END}")
#         else:
#             continue
#         limit = float(input("Limit offset price (Put 0 for market price): "))
#         if (limit == 0): print(f"{clrs.c.RED}WARNING! Some broker do not allow market order for stock price below $1 !{clrs.c.END}")
#         if (FENNEL):
#             f.createOrder("buy", ticker)
#         if (ROBIN):
#             print("[ROBINHOOD] INDIVIDUAL Account:")
#             r.rhPlaceOrder("buy",ticker)
#             if (ROBINROTH):
#                 print("[ROBINHOOD] ROTH IRA Account:")
#                 r.rhPlaceOrder("buy",ticker, os.getenv("ROBINROTH"))
#             if (ROBINIRA):
#                 print("[ROBINHOOD] TRADITIONAL IRA Account:")
#                 r.rhPlaceOrder("buy",ticker, os.getenv("ROBINIRA"))
#             #if (ROBINIRA):
#             #    r.rhBuyMarket(ticker, ROBINIRA)
#             r.switchValidation()
#         if (PUBLIC1):
#             print("[PUBLIC 1] PUBLIC INDIVIDUAL ACCOUNT")
#             p.placeOrder("buy", ticker)
#         if (PUBLIC2):
#             print("[PUBLIC 2] PUBLIC INDIVIDUAL ACCOUNT")
#             p.placeOrder("buy", ticker, True)
#         if (FIRSTRADE):
#             ft.buyOrder(ticker,limit)
#     elif x == 3:
#         os.system('cls')
#         ticker = input("Ticker name: ")
#         #offset = float(input("Limit Price: "))
#         if (FENNEL):
#             f.createOrder("sell", ticker)
#         if (ROBIN):
#             print("[ROBINHOOD] INDIVIDUAL Account:")
#             r.rhPlaceOrder("sell", ticker)
#             if (ROBINROTH):
#                 print("[ROBINHOOD] ROTH IRA Account:")
#                 r.rhPlaceOrder("sell",ticker, os.getenv("ROBINROTH"))
#             if (ROBINIRA):
#                 print("[ROBINHOOD] TRADITIONAL IRA Account:")
#                 r.rhPlaceOrder("sell",ticker, os.getenv("ROBINIRA"))
#         if (PUBLIC1):
#             print("[PUBLIC 1] PUBLIC INDIVIDUAL ACCOUNT")
#             p.placeOrder("sell", ticker)
#         if (PUBLIC2):
#             print("[PUBLIC 2] PUBLIC INDIVIDUAL ACCOUNT")
#             p.placeOrder("sell", ticker, True)
#         if (FIRSTRADE):
#             #print("[FIRSTRADE] FIRSTRADE Accounts")
#             ft.sellOrder(ticker)
#     elif x == 4:
#         os.system('cls')
#         ticker = input("Ticker name: ")
#         if (FENNEL):
#             f.getHolding(ticker=ticker, searchHighlight=True)
#         if (PUBLIC1):
#             p.getHolding(searchHighlight=True, ticker=ticker)
#         if (PUBLIC2):
#             p.getHolding(type=True, searchHighlight=True, ticker=ticker)


#     else:
#         os.system("pause")
#         exit()
index = None
while (index != 9):
    print("\n")
    option = ('[1] Get Position (ALL BROKERAGE)', '[2] Search stock exist on brokerage (WIP)', '[3] Buy Order', '[4] Sell Order', '[9] End')
    index = survey.routines.select('Select an option: ', options = option)
    if index == 0:
        os.system('cls')
        if (FENNEL):
            f.getHolding()
        if (ROBIN):
            r.getPosition(os.getenv("ROBINROTH"), os.getenv("ROBINIRA"))
        if (PUBLIC1):
            p.getHolding()
        if (PUBLIC2):
            p.getHolding(True)
        if (FIRSTRADE):
            ft.getHolding()
    elif index == 1:
        os.system('cls')
        ticker = survey.routines.input("Ticker name: ")
        if (FENNEL):
            f.getHolding(ticker=ticker, searchHighlight=True)
        if (PUBLIC1):
            p.getHolding(searchHighlight=True, ticker=ticker)
        if (PUBLIC2):
            p.getHolding(type=True, searchHighlight=True, ticker=ticker)
        if (FIRSTRADE):
            ft.getHolding(True, ticker)
    elif index == 2:
        os.system('cls')
        ticker = survey.routines.input("Ticker name: ")
        if (utils.YFgetStockPrice(ticker) != -1):
            print(f"{clrs.c.YELLOW}Current Price: {clrs.c.SELECTED}{round(utils.YFgetStockPrice(ticker),4)}{clrs.c.END}")
        else:
            continue
        limit = float(survey.routines.numeric("Limit offset price (Put 0 for market price): "))
        if (limit == 0): print(f"{clrs.c.RED}WARNING! Some broker do not allow market order for stock price below $1 !{clrs.c.END}")
        if (FENNEL):
            f.createOrder("buy", ticker.upper())
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
    elif index == 3:
        os.system('cls')
        ticker = survey.routines.input("Ticker name: ")
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
            print("[FIRSTRADE] FIRSTRADE Accounts")
            ft.sellOrder(ticker)
    else:
        os.system("pause")
        exit()