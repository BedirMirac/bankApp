from user import *
import library
from lang import *
from choosemoney import getmoneynumber
from doviz import *


def money_transfer(username):
    money = getmoneynumber()
    lang = get_dil()
    print(f"{lang["komisyonuyarı"]}")
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    tl = balancetr()
    usd = balanceusd()
    eur = balanceeur()
    u = search_username(username)
    ud = search_userdolar(username)
    ue = search_usereur(username)

    if money == 1:
        u = search_username(username)
        bakiye = u[5]
        bank_balance = tl
    elif money == 2:
        ud = search_userdolar(username)
        bakiye = ud[4]
        bank_balance = usd
    elif money == 3:
        ue = search_usereur(username)
        bakiye = ue[4]
        bank_balance = eur

    while True:
        try:
            reciever = input(f"{lang["reciever"]}")
            if money == 1:
                control = search_username(reciever)
            elif money == 2:
                control = search_userdolar(reciever)
            elif money == 3:
                control =search_usereur(reciever)

            if control is None and money == 1:
                print(f"{lang["not_found"]}")
            elif control is None and money == 2:
                var_mi = search_username(reciever)
                if var_mi is None:
                    print(f"{lang["not_found"]}")
                else:
                    print(f"{lang["dolarhesapyok"]}")
            elif control is None and money == 3:
                var_mi = search_username(reciever)
                if var_mi is None:
                    print(f"{lang["not_found"]}")
                else:
                    print(f"{lang["eurohesapyok"]}")
            elif username == reciever:
                acc = input(f"{lang["whicacc"]}(TRY/USD/EUR) :")
                acc = acc.upper()
                while True:
                    if money == 1 and acc == "USD":
                        if ud is None:
                            print(f"{lang["urnousdacc"]}")
                            break
                        miktar = float(input(f"{lang["send"]}"))
                        print(f"{lang["usdkarşılık"]}")
                        if miktar > bakiye:
                            print(f"{lang["send2"]}")
                            continue
                        else:
                            rd = search_userdolar(username)
                            rdbakiye = rd[4]
                            if miktar + miktar * 0.1 > bakiye:
                                print(f"{lang["komisyon"]}")
                            else:
                                bakiye -= miktar
                                bakiye -= miktar * 0.1
                                rdbakiye += miktar / dolardovizfiyat()
                                bank_balance += miktar * 0.1
                                cursor.execute("UPDATE bankBalance SET bankBalanceTRY = ?", (bank_balance,))
                                cursor.execute("UPDATE dolar SET dolar_balance = ? WHERE username = ?",(rdbakiye,username))
                                cursor.execute("UPDATE data SET bakiye = ? WHERE username = ?",(bakiye,username))
                                break
                    elif money == 1 and acc == "EUR":
                        if ue is None:
                            print(f"{lang["urnoeuracc"]}")
                            break
                        miktar = float(input(f"{lang["send"]}"))
                        print(f"{lang["eurkarşılık"]}")
                        if miktar > bakiye:
                            print(f"{lang["send2"]}")
                            continue
                        else:
                            re = search_usereur(username)
                            rebakiye = re[4]
                            if miktar + miktar * 0.1 > bakiye:
                                print(f"{lang["komisyon"]}")
                            else:
                                bakiye -= miktar
                                bakiye -= miktar * 0.1
                                rebakiye += miktar / eurdovizfiyat()
                                bank_balance += miktar * 0.1
                                cursor.execute("UPDATE bankBalance SET bankBalanceTRY = ?", (bank_balance,))

                                cursor.execute("UPDATE euro SET euro_balance = ? WHERE username = ?",(rebakiye, username))
                                cursor.execute("UPDATE data SET bakiye = ? WHERE username = ?", (bakiye, username))
                                break
                    elif money == 2 and acc == "EUR":
                        if ue is None:
                            print(f"{lang["urnoeuracc"]}")
                            break
                        miktar = float(input(f"{lang["send"]}"))
                        print(f"{lang["eurkarşılık"]}")
                        if miktar > bakiye:
                            print(f"{lang["send2"]}")
                            continue
                        else:
                            re = search_usereur(username)
                            rebakiye = re[4]
                            if miktar + miktar * 0.1 > bakiye:
                                print(f"{lang["komisyon"]}")
                            else:
                                bakiye -= miktar
                                bakiye -= miktar * 0.1
                                rebakiye += miktar / eurdolar()
                                bank_balance += miktar * 0.1
                                cursor.execute("UPDATE bankBalance SET bankBalanceUSD = ?", (bank_balance,))

                                cursor.execute("UPDATE euro SET euro_balance = ? WHERE username = ?",(rebakiye, username))
                                cursor.execute("UPDATE dolar SET dolar_balance = ? WHERE username = ?", (bakiye, username))
                                break
                    elif money == 2 and acc == "TRY":
                        miktar = float(input(f"{lang["send"]}"))
                        print(f"{lang["tlkarşılık"]}")
                        if miktar > bakiye:
                            print(f"{lang["send2"]}")
                            continue
                        else:
                            r = search_username(username)
                            rbakiye = r[5]
                            if miktar + miktar * 0.1 > bakiye:
                                print(f"{lang["komisyon"]}")
                            else:
                                bakiye -= miktar
                                bakiye -= miktar * 0.1
                                rbakiye += miktar * dolardovizfiyat()
                                bank_balance += miktar * 0.1
                                cursor.execute("UPDATE bankBalance SET bankBalanceUSD = ?", (bank_balance,))

                                cursor.execute("UPDATE data SET bakiye = ? WHERE username = ?",(rbakiye, username))
                                cursor.execute("UPDATE dolar SET dolar_balance = ? WHERE username = ?", (bakiye, username))
                                break
                    elif money == 3 and acc == "TRY":
                        miktar = float(input(f"{lang["send"]}"))
                        print(f"{lang["tlkarşılık"]}")
                        if miktar > bakiye:
                            print(f"{lang["send2"]}")
                            continue
                        else:
                            r = search_username(username)
                            rbakiye = r[5]
                            if miktar + miktar * 0.1 > bakiye:
                                print(f"{lang["komisyon"]}")
                            else:
                                bakiye -= miktar
                                bakiye -= miktar * 0.1
                                rbakiye += miktar * eurdovizfiyat()
                                bank_balance += miktar * 0.1
                                cursor.execute("UPDATE bankBalance SET bankBalanceEUR = ?", (bank_balance,))

                                cursor.execute("UPDATE data SET bakiye = ? WHERE username = ?",(rbakiye, username))
                                cursor.execute("UPDATE euro SET euro_balance = ? WHERE username = ?", (bakiye, username))
                                break

                    elif money == 3 and acc == "USD":
                        if ud is None:
                            print(f"{lang["urnousdacc"]}")
                            break
                        miktar = float(input(f"{lang["send"]}"))
                        print(f"{lang["usdkarşılık"]}")
                        if miktar > bakiye:
                            print(f"{lang["send2"]}")
                            continue
                        else:
                            rd = search_userdolar(username)
                            rdbakiye = rd[4]
                            if miktar + miktar * 0.1 > bakiye:
                                print(f"{lang["komisyon"]}")
                            else:
                                bakiye -= miktar
                                bakiye -= miktar * 0.1
                                rdbakiye += miktar * dolareuro()
                                bank_balance += miktar * 0.1
                                cursor.execute("UPDATE bankBalance SET bankBalanceEUR = ?", (bank_balance,))

                                cursor.execute("UPDATE dolar SET dolar_balance = ? WHERE username = ?",(rdbakiye, username))
                                cursor.execute("UPDATE euro SET euro_balance = ? WHERE username = ?", (bakiye, username))
                                break

                    elif money == 1 and acc == "TRY":
                        print(f"{lang["sameacc"]}")
                        break
                    elif money == 2 and acc == "USD":
                        print(f"{lang["sameacc"]}")
                        break
                    elif money == 3 and acc == "EUR":
                        print(f"{lang["sameacc"]}")
                        break
                    else:
                        print(f"uhavent")
                        break

                break

            else:
                rd = search_userdolar(reciever)
                re = search_usereur(reciever)
                acc2 = input(f"{lang["rhesap"]}")
                acc2 = acc2.upper()
                if money == 1 and acc2 == "USD":
                    if rd is None:
                        print(f"{lang["rusdno"]}")
                        break
                    miktar = float(input(f"{lang["send"]}"))
                    print(f"{lang["usdkarşılık"]}")
                    if miktar > bakiye:
                        print(f"{lang["send2"]}")
                        continue
                    else:
                        rd = search_userdolar(username)
                        rdbakiye = rd[4]
                        if miktar + miktar * 0.1 > bakiye:
                            print(f"{lang["komisyon"]}")
                        else:
                            bakiye -= miktar
                            bakiye -= miktar * 0.1
                            rdbakiye += miktar / dolardovizfiyat()
                            bank_balance += miktar * 0.1
                            cursor.execute("UPDATE bankBalance SET bankBalanceTRY = ?", (bank_balance,))

                            cursor.execute("UPDATE dolar SET dolar_balance = ? WHERE username = ?", (rdbakiye, reciever))
                            cursor.execute("UPDATE data SET bakiye = ? WHERE username = ?", (bakiye, username))
                            break
                elif money == 1 and acc2 == "EUR":
                    if re is None:
                        print(f"{lang["rnoeur"]}")
                        break
                    miktar = float(input(f"{lang["send"]}"))
                    print(f"{lang["eurkarşılık"]}")
                    if miktar > bakiye:
                        print(f"{lang["send2"]}")
                        continue
                    else:
                        re = search_usereur(username)
                        rebakiye = re[4]
                        if miktar + miktar * 0.1 > bakiye:
                            print(f"{lang["komisyon"]}")
                        else:
                            bakiye -= miktar
                            bakiye -= miktar * 0.1
                            rebakiye += miktar / eurdovizfiyat()
                            bank_balance += miktar * 0.1
                            cursor.execute("UPDATE bankBalance SET bankBalanceTRY = ?", (bank_balance,))

                            cursor.execute("UPDATE euro SET euro_balance = ? WHERE username = ?",(rebakiye, reciever))
                            cursor.execute("UPDATE data SET bakiye = ? WHERE username = ?", (bakiye, username))
                            break
                elif money == 2 and acc2 == "EUR":
                    if re is None:
                        print(f"{lang["rnoeur"]}")
                        break
                    miktar = float(input(f"{lang["send"]}"))
                    print(f"{lang["eurkarşılık"]}")
                    if miktar > bakiye:
                        print(f"{lang["send2"]}")
                        continue
                    else:
                        re = search_usereur(username)
                        rebakiye = re[4]
                        if miktar + miktar * 0.1 > bakiye:
                            print(f"{lang["komisyon"]}")
                        else:
                            bakiye -= miktar
                            bakiye -= miktar * 0.1
                            rebakiye += miktar / eurdolar()
                            bank_balance += miktar * 0.1
                            cursor.execute("UPDATE bankBalance SET bankBalanceUSD = ?", (bank_balance,))

                            cursor.execute("UPDATE euro SET euro_balance = ? WHERE username = ?",(rebakiye, reciever))
                            cursor.execute("UPDATE dolar SET dolar_balance = ? WHERE username = ?", (bakiye, username))
                            break
                elif money == 2 and acc2 == "TRY":
                    miktar = float(input(f"{lang["send"]}"))
                    print(f"{lang["tlkarşılık"]}")
                    if miktar > bakiye:
                        print(f"{lang["send2"]}")
                        continue
                    else:
                        r = search_username(username)
                        rbakiye = r[5]
                        if miktar + miktar * 0.1 > bakiye:
                            print(f"{lang["komisyon"]}")
                        else:
                            bakiye -= miktar
                            bakiye -= miktar * 0.1
                            rbakiye += miktar * dolardovizfiyat()
                            bank_balance += miktar * 0.1
                            cursor.execute("UPDATE bankBalance SET bankBalanceUSD = ?", (bank_balance,))

                            cursor.execute("UPDATE data SET bakiye = ? WHERE username = ?",(rbakiye, reciever))
                            cursor.execute("UPDATE dolar SET dolar_balance = ? WHERE username = ?", (bakiye, username))
                            break
                elif money == 3 and acc2 == "USD":
                    if rd is None:
                        print(f"{lang["rusdno"]}")
                        break
                    miktar = float(input(f"{lang["send"]}"))
                    print(f"{lang["usdkarşılık"]}")
                    if miktar > bakiye:
                        print(f"{lang["send2"]}")
                        continue
                    else:
                        rd = search_userdolar(username)
                        rdbakiye = rd[4]
                        if miktar + miktar * 0.1 > bakiye:
                            print(f"{lang["komisyon"]}")
                        else:
                            bakiye -= miktar
                            bakiye -= miktar * 0.1
                            rdbakiye += miktar * dolareuro()
                            bank_balance += miktar * 0.1
                            cursor.execute("UPDATE bankBalance SET bankBalanceEUR = ?", (bank_balance,))

                            cursor.execute("UPDATE dolar SET dolar_balance = ? WHERE username = ?",(rdbakiye, reciever))
                            cursor.execute("UPDATE euro SET euro_balance = ? WHERE username = ?", (bakiye, username))
                            break
                elif money == 3 and acc2 == "TRY":
                    miktar = float(input(f"{lang["send"]}"))
                    print(f"{lang["tlkarşılık"]}")
                    if miktar > bakiye:
                        print(f"{lang["send2"]}")
                        continue
                    else:
                        r = search_username(username)
                        rbakiye = r[5]
                        if miktar + miktar * 0.1 > bakiye:
                            print(f"{lang["komisyon"]}")
                        else:
                            bakiye -= miktar
                            bakiye -= miktar * 0.1
                            rbakiye += miktar * eurdovizfiyat()
                            bank_balance += miktar * 0.1
                            cursor.execute("UPDATE bankBalance SET bankBalanceEUR = ?", (bank_balance,))

                            cursor.execute("UPDATE data SET bakiye = ? WHERE username = ?",(rbakiye, reciever))
                            cursor.execute("UPDATE euro SET euro_balance = ? WHERE username = ?", (bakiye, username))
                            break
                else:

                    while True:
                        if money == 1:
                            r = search_username(reciever)
                            rbakiye = r[5]
                        elif money == 2:
                            rd = search_userdolar(reciever)
                            rbakiye = rd[4]
                        elif money == 3:
                            re = search_usereur(username)
                            rbakiye = re[4]
                        miktar = float(input(f"{lang["send"]}"))

                        if miktar > bakiye:
                            print(f"{lang["send2"]}")
                            continue
                        else:
                            if miktar + miktar*0.1 > bakiye:
                                print(f"{lang["komisyon"]}")
                            else:
                                bakiye -= miktar
                                bakiye -= miktar*0.1
                                rbakiye += miktar
                                bank_balance += miktar * 0.1
                                if money == 1:
                                    cursor.execute("UPDATE bankBalance SET bankBalanceTRY = ?", (bank_balance,))
                                    cursor.execute("UPDATE data SET bakiye = ? WHERE username = ?",(rbakiye,reciever))
                                    cursor.execute("UPDATE data SET bakiye = ? WHERE username = ?",(bakiye,username))
                                    break
                                elif money == 2:
                                    cursor.execute("UPDATE bankBalance SET bankBalanceUSD = ?", (bank_balance,))
                                    cursor.execute("UPDATE dolar SET dolar_balance = ? WHERE username = ?",(rbakiye,reciever))
                                    cursor.execute("UPDATE dolar SET dolar_balance = ? WHERE username = ?",(bakiye,username))
                                    break
                                if money == 3:
                                    cursor.execute("UPDATE bankBalance SET bankBalanceEUR = ?", (bank_balance,))
                                    cursor.execute("UPDATE euro SET euro_balance = ? WHERE username = ?",(rbakiye,reciever))
                                    cursor.execute("UPDATE euro SET euro_balance = ? WHERE username = ?",(bakiye,username))
                                    break
                break
        except ValueError:
            print(f"{lang["b"]}")

    con.commit()
    con.close()




