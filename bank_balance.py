import sqlite3

def bankBalance():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS bankBalance( 
    id INT PRIMARY KEY,
    bankBalanceTRY REAL,
    bankBalanceUSD REAL,
    bankBalanceEUR REAL
    ) 
    """)
    con.commit()
    con.close()

def insertbalance(tl = 100000, usd= 200000, eur = 200000 ):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO bankBalance (bankBalanceTRY, bankBalanceUSD, bankBalanceEUR) VALUES (?,?,?)",(tl,usd,eur))
    con.commit()
    con.close()


def balancetr():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM bankBalance")
    allBalance = cursor.fetchone()
    trBalance = allBalance[1]

    return trBalance
    con.close()


def balanceusd():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM bankBalance")
    allBalance = cursor.fetchone()
    usdBalance = allBalance[2]

    return usdBalance
    con.close()


def balanceeur():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM bankBalance")
    allBalance = cursor.fetchone()
    eurBalance = allBalance[3]

    return eurBalance
    con.close()
