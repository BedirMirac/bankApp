import sqlite3
from choosemoney import getmoneynumber
from faiz import *
import library
from lang import *
from doviz import *
from bank_balance import *

def table():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS data (
        id integer PRIMARY KEY,
        name text,
        surname text,
        username text UNIQUE,
        password text,
        bakiye real,
        kredi real
    )""")
    con.commit()
    con.close()


def insert(name, surname, username, password, bakiye=0.0, kredi=0.0):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    add_command = "INSERT INTO data (name, surname, username, password, bakiye, kredi) VALUES (?, ?, ?, ?, ?, ?)"
    data = (name, surname, username, password, bakiye, kredi)

    cursor.execute(add_command, data)

    con.commit()
    con.close()

def upd_password(username,newPassword):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    upd_command = ("""UPDATE data SET password = '{}' where username = '{}'""")
    cursor.execute(upd_command.format(newPassword, username))

    con.commit()
    con.close()

def delete_user(username):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    dlt_command = ("DELETE FROM data where username = '{}' ")

    cursor.execute(dlt_command.format(username))
    con.commit()
    con.close()


def search_username(username):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM data WHERE username = ?", (username,))
    user = cursor.fetchone()

    con.close()

    if user is None:
        return None

    if user[5] is None:
        user = list(user)
        user[5] = 0.0
        user = tuple(user)

    return user


def update_balance(username, bakiye):
    lang = get_dil()
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    try:
        cursor.execute("""UPDATE data SET bakiye = ? WHERE username = ?""", (bakiye, username))
        con.commit()
        print(f"{lang["your_balance"]} {bakiye:.2f}₺")
    except Exception as e:
        con.rollback()
        print(f"{lang["error_balance"]} {e}")
    finally:
        con.close()


def kredisorgu(username):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    cursor.execute("""SELECT kredi FROM data WHERE username = ?""", (username,))
    krediborc = cursor.fetchone()
    con.close()

    if krediborc is None or krediborc[0] is None:
        return 0.0
    return krediborc[0]






def paykredi(username):
    money = getmoneynumber()
    lang = get_dil()
    tl = balancetr()
    usd = balanceusd()
    eur = balanceeur()
    if money == 1:
        borc = kredisorgu(username)
        bankbalance = tl
    elif money == 2:
        borc = kredisorguusd(username)
        bankbalance = usd
    elif money == 3:
        borc = kredisorgueur(username)
        bankbalance = eur
    if borc == 0.0:
        print(f"{lang["kredi0"]}")
        return
    while True:
        try:
            miktar = float(input(f"{lang["kredi1"]}"))
            if money == 1:
                u = search_username(username)
                bakiye = u[5]
            elif money == 2:
                ud = search_userdolar(username)
                bakiye = ud[4]
            elif money == 3:
                ue = search_usereur(username)
                bakiye = ue[4]
            break
        except ValueError:
            print(f"{lang["b"]}")

    if miktar > bakiye:
        print(f"{lang["kredi2"]}")
        return

    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    try:
        if money == 1:
            bankbalance += miktar
            cursor.execute("UPDATE bankBalance SET bankBalanceTRY = ?",(bankbalance,))
            yeni_borc = borc - miktar
            cursor.execute("""UPDATE data SET kredi = ? WHERE username = ?""", (yeni_borc, username))

            yeni_bakiye = bakiye - miktar
            cursor.execute("""UPDATE data SET bakiye = ? WHERE username = ?""", (yeni_bakiye, username))

            con.commit()

            yeni_kredi = kredisorgu(username)
            yeni_u = search_username(username)
            bakiye_son = yeni_u[5]

            print(f"{lang["kredi3"]} {bakiye_son:.2f}₺, {lang["kredi4"]} {yeni_kredi:.2f}₺")

            update_balance(username, bakiye_son)
        elif money == 2:
            bankbalance += miktar
            cursor.execute("UPDATE bankBalance SET bankBalanceUSD = ?", (bankbalance,))
            yeni_borc = borc - miktar
            cursor.execute("""UPDATE dolar SET dolar_kredi = ? WHERE username = ?""", (yeni_borc, username))

            yeni_bakiye = bakiye - miktar
            cursor.execute("""UPDATE dolar SET dolar_balance = ? WHERE username = ?""", (yeni_bakiye, username))

            con.commit()

            yeni_kredi = kredisorguusd(username)
            yeni_ud = search_userdolar(username)
            bakiye_son = yeni_ud[4]

            print(f"{lang["kredi3"]} {bakiye_son:.2f}$, {lang["kredi4"]} {yeni_kredi:.2f}$")

            update_balanceusd(username, bakiye_son)
        elif money == 3:
            bankbalance += miktar
            cursor.execute("UPDATE bankBalance SET bankBalanceEUR = ?", (bankbalance,))
            yeni_borc = borc - miktar
            cursor.execute("""UPDATE euro SET euro_kredi = ? WHERE username = ?""", (yeni_borc, username))

            yeni_bakiye = bakiye - miktar
            cursor.execute("""UPDATE euro SET euro_balance = ? WHERE username = ?""", (yeni_bakiye, username))

            con.commit()

            yeni_kredi = kredisorgueur(username)
            yeni_ue = search_usereur(username)
            bakiye_son = yeni_ue[4]

            print(f"{lang["kredi3"]} {bakiye_son:.2f}€, {lang["kredi4"]} {yeni_kredi:.2f}€")

            update_balanceeur(username, bakiye_son)

    except Exception as e:
        con.rollback()
        print(f"{lang["hata"]} {e}")
    finally:
        con.close()









def kredial(username):
    money = getmoneynumber()
    tl = balancetr()
    usd = balanceusd()
    eur = balanceeur()
    if money == 1:
        bank_balance = tl
    elif money == 2:
        bank_balance = usd
    elif money == 3:
        bank_balance = eur

    lang = get_dil()
    while True:
        try:
            kredi = float(input(f"{lang["kredi5"]}"))
            if kredi > bank_balance * 0.3:
                if money == 1:
                    print(f"{lang["tutarfazla"]} {(bank_balance * 0.3)}₺")
                    continue
                elif money == 2:
                    print(f"{lang["tutarfazla"]} {(bank_balance * 0.3)}$")
                    continue
                elif money == 3:
                    print(f"{lang["tutarfazla"]} {(bank_balance * 0.3)}€")
                    continue
            kacay = int(input(f"{lang["kredi6"]}"))
            break
        except ValueError:
            print(f"{lang["b"]}")

    if kacay == 0:
        borc = faiz3m(kredi)
    elif kacay == 1:
        borc = faiz6m(kredi)
    elif kacay == 2:
        borc = faiz12m(kredi)
    elif kacay == 3:
        borc = faiz24m(kredi)
    elif kacay == 4:
        borc = faiz36m(kredi)
    else:
        print(f"{lang['invalid_choice']}")
        return
    if money == 1:
        existing_credit = kredisorgu(username)
    elif money == 2:
        existing_credit = kredisorguusd(username)
    elif money == 3:
        existing_credit = kredisorgueur(username)

    if existing_credit > 0:
        print(f"{lang['existing_credit_warning']}")
        return

    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    try:
        if money == 1:
            bank_balance -= borc
            cursor.execute("""UPDATE data SET kredi = ? WHERE username = ?""", (borc, username))
            cursor.execute("UPDATE bankBalance SET bankBalanceTRY = ?",(bank_balance,))

            u = search_username(username)
            bakiye = u[5] + kredi

            cursor.execute("""UPDATE data SET bakiye = ? WHERE username = ?""", (bakiye, username))

            con.commit()

            yeni_kredi = kredisorgu(username)
            yeni_u = search_username(username)
            yeni_bakiye = yeni_u[5]

            print(f"{lang["kredi7"]} {yeni_bakiye:.2f}₺, {lang["kredi8"]} {yeni_kredi:.2f}₺")

            update_balance(username, yeni_bakiye)
        elif money == 2:
            bank_balance -= borc
            cursor.execute("UPDATE bankBalance SET bankBalanceUSD = ?", (bank_balance,))
            cursor.execute("""UPDATE dolar SET dolar_kredi = ? WHERE username = ?""",(borc,username))

            ud = search_userdolar(username)
            bakiye = ud[4] + kredi

            cursor.execute("""UPDATE dolar SET dolar_balance = ? WHERE username = ?""",(bakiye,username))

            con.commit()

            yeni_kredi = kredisorguusd(username)
            yeni_ud = search_userdolar(username)
            yeni_bakiye = yeni_ud[4]

            print(f"{lang["kredi7"]} {yeni_bakiye:.2f}$, {lang["kredi8"]} {yeni_kredi:.2f}$")
            update_balanceusd(username, yeni_bakiye)
        elif money == 3:
            bank_balance -= borc
            cursor.execute("UPDATE bankBalance SET bankBalanceEUR = ?", (bank_balance,))
            cursor.execute("""UPDATE euro SET euro_kredi = ? WHERE username = ?""", (borc, username))

            ue = search_usereur(username)
            bakiye = ue[4] + kredi

            cursor.execute("""UPDATE euro SET euro_balance = ? WHERE username = ?""", (bakiye, username))

            con.commit()

            yeni_kredi = kredisorgueur(username)
            yeni_ue = search_usereur(username)
            yeni_bakiye = yeni_ue[4]

            print(f"{lang["kredi7"]} {yeni_bakiye:.2f}€, {lang["kredi8"]} {yeni_kredi:.2f}€")
            update_balanceeur(username, yeni_bakiye)

    except Exception as e:
        con.rollback()
        print(f"{lang["hata"]} {e}")
    finally:
        con.close()



def dolar():

    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS dolar(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   surname TEXT,
                   username TEXT,
                   dolar_balance REAL,
                   dolar_kredi REAL
                   )""")

    con.commit()
    con.close()

def euro():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS euro(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       surname TEXT,
                       username TEXT,
                       euro_balance REAL,
                       euro_kredi REAL
                       )""")

    con.commit()
    con.close()


def dolaruser(name, surname, username, dolar_balance = 0.0, dolar_kredi = 0.0):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    u = search_username(username)

    dolar_command = "INSERT INTO dolar (name, surname, username, dolar_balance, dolar_kredi) VALUES (?, ?, ?, ?, ?)"
    dolar_data = (name, surname, username, dolar_balance, dolar_kredi)
    cursor.execute(dolar_command,dolar_data)

    con.commit()
    con.close()


def euruser(name ,surname, username, euro_balance = 0.0, euro_kredi = 0.0):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    u = search_username(username)

    eur_command = "INSERT INTO euro (name, surname, username, euro_balance, euro_kredi) VALUES (?, ?, ?, ?, ?)"
    euro_data = (name, surname, username, euro_balance, euro_kredi)
    cursor.execute(eur_command, euro_data)

    con.commit()
    con.close()

def search_userdolar(username):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM dolar WHERE username = ?", (username,))
    user = cursor.fetchone()

    con.close()

    if user is None:
        return None

    return user

def search_usereur(username):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM euro WHERE username = ?", (username,))
    user = cursor.fetchone()

    con.close()

    if user is None:
        return None

    return user

def update_balanceusd(username, bakiye):
    lang = get_dil()
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    try:
        cursor.execute("""UPDATE dolar SET dolar_balance = ? WHERE username = ?""", (bakiye, username))
        con.commit()
        print(f"{lang["your_balance"]} {bakiye:.2f}$")
    except Exception as e:
        con.rollback()
        print(f"{lang["error_balance"]} {e}")
    finally:
        con.close()


def update_balanceeur(username, bakiye):
    lang = get_dil()
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    try:
        cursor.execute("""UPDATE euro SET euro_balance = ? WHERE username = ?""", (bakiye, username))
        con.commit()
        print(f"{lang["your_balance"]} {bakiye:.2f}€")
    except Exception as e:
        con.rollback()
        print(f"{lang["error_balance"]} {e}")
    finally:
        con.close()

def kredisorguusd(username):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    cursor.execute("""SELECT dolar_kredi FROM dolar WHERE username = ?""", (username,))
    krediborc = cursor.fetchone()
    con.close()

    if krediborc is None or krediborc[0] is None:
        return 0.0
    return krediborc[0]


def kredisorgueur(username):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    cursor.execute("""SELECT euro_kredi FROM euro WHERE username = ?""", (username,))
    krediborc = cursor.fetchone()
    con.close()

    if krediborc is None or krediborc[0] is None:
        return 0.0
    return krediborc[0]


def delete_acc(username, parabirimi):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    u = search_username(username)
    ud = search_userdolar(username)
    ue = search_usereur(username)
    bakiye = u[5]
    if parabirimi == "euro":
        query = "DELETE FROM {} WHERE username = ?".format(parabirimi)
        cursor.execute(query, (username,))
    elif parabirimi == "dolar":
        query = "DELETE FROM {} WHERE username = ?".format(parabirimi)
        cursor.execute(query, (username,))


    con.commit()
    con.close()

