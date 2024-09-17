import library
from lang import *


money = 1
def set_money(para):
    global money
    money = para

def choosemoney():
    lang = get_dil()
    while True:
        moneyinput = input(f"{lang["moneyinput"]}")
        moneyinput = moneyinput.upper()
        if moneyinput == "TRY":
            set_money(1)
            return "TRY"
        elif moneyinput == "USD":
            set_money(2)
            return "USD"
        elif moneyinput == "EUR":
            set_money(3)
            return "EUR"
        else:
            print(f"{lang["hataligiris"]}")
            continue
        break




def getmoneynumber():
    global money
    return money

