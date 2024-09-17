import sqlite3
from user import *
from lang import *
import time
import random
from choosemoney import getmoneynumber


def kumar(username):
    money = getmoneynumber()
    lang = get_dil()
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    tl = balancetr()
    usd = balanceusd()
    eur = balanceeur()

    if money == 1:
        u = search_username(username)
        bakiye = u[5]
        bankbalance = tl
    elif money == 2:
        ud = search_userdolar(username)
        bakiye = ud[4]
        bankbalance = usd
    elif money == 3:
        ue = search_usereur(username)
        bakiye = ue[4]
        bankbalance = eur

    while True:
        try:
            miktar = int(input(f"{lang["kumar"]}"))
            if miktar > bakiye:
                print(f"{lang["kumar2"]}")
                continue
            else:
                zar = random.randint(1,6)
                zar_at = int(input(f"{lang["kumar3"]}"))
                if not 1 <= zar_at <= 6:
                    print(f"{lang["dicenum"]}")
                    continue
                else:
                    print(f"{lang["kumar4"]}")
                    time.sleep(3)
                    ihtimal = random.random()
                    if ihtimal < 0.7:
                        zar = random.choice([x for x in range(1, 7) if x != zar_at])  # Araştır
                        print(f"{lang["dice"]}",zar)
                    else:
                        zar = zar_at
                    if zar_at == zar:
                        bakiye += miktar
                        bankbalance -= miktar
                        if money == 1:
                            cursor.execute("UPDATE bankBalance SET bankBalanceTRY = ?", (bankbalance,))
                            cursor.execute("UPDATE data SET bakiye = ? WHERE username = ?",(bakiye,username))
                        elif money == 2:
                            cursor.execute("UPDATE bankBalance SET bankBalanceUSD = ?", (bankbalance,))
                            cursor.execute("UPDATE dolar SET dolar_balance = ? WHERE username = ?", (bakiye, username))
                        elif money == 3:
                            cursor.execute("UPDATE bankBalance SET bankBalanceEUR = ?", (bankbalance,))
                            cursor.execute("UPDATE euro SET euro_balance = ? WHERE username = ?", (bakiye, username))
                        devam = input(f"{lang["kumar5"]}{bakiye:.2f}₺. {lang["kumar6"]}")
                        devam = devam.upper()
                        if devam == f"{lang["h"]}":
                            break
                        else:
                            continue
                    else:
                        bakiye -= miktar
                        bankbalance += miktar
                        if money == 1:
                            cursor.execute("UPDATE bankBalance SET bankBalanceTRY = ?", (bankbalance,))
                            cursor.execute("UPDATE data SET bakiye = ? WHERE username = ?", (bakiye, username))
                            print(f"{lang["kumar7"]} {lang["your_balance"]} {bakiye:.2f}₺.")
                        elif money == 2:
                            cursor.execute("UPDATE bankBalance SET bankBalanceUSD = ?", (bankbalance,))
                            cursor.execute("UPDATE dolar SET dolar_balance = ? WHERE username = ?", (bakiye, username))
                            print(f"{lang["kumar7"]} {lang["your_balance"]} {bakiye:.2f}$.")
                        elif money == 3:
                            cursor.execute("UPDATE bankBalance SET bankBalanceEUR = ?", (bankbalance,))
                            cursor.execute("UPDATE euro SET euro_balance = ? WHERE username = ?", (bakiye, username))
                            print(f"{lang["kumar7"]} {lang["your_balance"]} {bakiye:.2f}€.")
                        devam2 = input(f"{lang["kumar8"]}")
                        devam2 = devam2.upper()
                        if devam2 == f"{lang["h"]}":
                            break
                        else:
                            continue
        except ValueError:
            print(f"{lang["b"]}")

    con.commit()
    con.close()







