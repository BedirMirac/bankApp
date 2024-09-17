import library
from kumar import *
from user import *
from money_transfer import *
import faiz
from lang import *
from datetime import datetime
import locale
from doviz import *
from choosemoney import *
locale.setlocale(locale.LC_ALL, '')
date = datetime.now()

table()
euro()
dolar()
bankBalance()


def para_islemleri(username):
    lang = get_dil()
    choosemoney()
    money = getmoneynumber()
    ud = search_userdolar(username)
    ue = search_usereur(username)
    u = search_username(username)
    if u is None:
        lang = get_dil()
        print(f"{lang["not_found"]}")
        return
    name = u[1]
    surname = u[2]
    if money == 2:
        if ud is None:
            dolar()
            dolaruser(name, surname, username)
            print(f"{lang["dolarhesap"]} {lang["your_balance"]} 0.0$ ")
    if money == 3:
        if ue is None:
            euro()
            euruser(name, surname, username)
            print(f"{lang["eurohesap"]}{lang["your_balance"]} 0.0€ ")




    while True:
        lang = get_dil()

        while True:
            ud = search_userdolar(username)
            ue = search_usereur(username)
            u = search_username(username)
            if money == 1:
                bakiye = u[5]
                if bakiye is None:
                    bakiye = 0.0
                break
            elif money == 2:
                if ud is None:
                    bakiye = 0.0
                else:
                    bakiye = ud[4]
                if bakiye is None:
                    bakiye = 0.0
                break
            elif money == 3:
                if ue is None:
                    bakiye = 0.0
                else:
                     bakiye = ue[4]
                if bakiye is None:
                    bakiye = 0.0
                break
            else:
                print(f"{lang["hataligiris"]}")
                continue



        try:

            if money == 1:
                kredi = kredisorgu(username)
            elif money == 2:
                kredi = kredisorguusd(username)
            elif money == 3:
                kredi = kredisorgueur(username)


            islem = int(input(f""" {lang["select_action"]}
                            {lang["changemoney"]}
                            {lang["money1"]}
                            {lang["money2"]}
                            {lang["faiz"]}
                            {lang["kredi"]}
                            {lang["money_transfer"]}
                            {lang["kumar_menu"]}
                            {lang["doviz"]}
                            {lang["delete_acc"]}
                            {lang["change_pass"]}
                            {lang["money3"]}
                                :"""))
            if islem == 1:
                try:
                    miktar = float(input(f"{lang["enter_withdrawal_amount"]}"))
                    if miktar > bakiye:
                        print(f"{lang["a"]}")
                    else:
                        bakiye -= miktar
                except ValueError:
                    print(f"{lang["invalid_numeric_value"]}")

            elif islem == 2:
                try:
                    miktar = float(input(f"{lang["enter_deposit_amount"]}"))
                    bakiye += miktar
                except ValueError:
                    print(f"{lang["invalid_numeric_value"]}")
            elif islem == 0:
                print(f"{lang["menu_closing"]}")
                break

            elif islem == 3:
                while True:
                    miktar = int(input(f"""{lang["faiz3"]}"""))
                    if miktar > bakiye:
                        print(f"{lang["faiz_a"]}")
                    else:
                        break
                faizislem = int(input(f"""{lang["faiz2"]}"""))
                bakiye -= miktar
                if faizislem == 1:
                    miktar = faiz.faiz3m(miktar)
                    bakiye += miktar
                    if money == 1:
                        print(f"{lang["your_balance"]} {bakiye:.2f}₺")
                    elif money == 2:
                        print(f"{lang["your_balance"]} {bakiye:.2f}$")
                    elif money == 3:
                        print(f"{lang["your_balance"]} {bakiye:.2f}€")
                elif faizislem == 2:
                    miktar = faiz.faiz6m(miktar)
                    bakiye += miktar
                    if money == 1:
                        print(f"{lang["your_balance"]} {bakiye:.2f}₺")
                    elif money == 2:
                        print(f"{lang["your_balance"]} {bakiye:.2f}$")
                    elif money == 3:
                        print(f"{lang["your_balance"]} {bakiye:.2f}€")
                elif faizislem == 3:
                    miktar = faiz.faiz12m(miktar)
                    bakiye += miktar
                    if money == 1:
                        print(f"{lang["your_balance"]} {bakiye:.2f}₺")
                    elif money == 2:
                        print(f"{lang["your_balance"]} {bakiye:.2f}$")
                    elif money == 3:
                        print(f"{lang["your_balance"]} {bakiye:.2f}€")
                elif faizislem == 4:
                    miktar = faiz.faiz24m(miktar)
                    bakiye += miktar
                    if money == 1:
                        print(f"{lang["your_balance"]} {bakiye:.2f}₺")
                    elif money == 2:
                        print(f"{lang["your_balance"]} {bakiye:.2f}$")
                    elif money == 3:
                        print(f"{lang["your_balance"]} {bakiye:.2f}€")
                elif faizislem == 5:
                    miktar = faiz.faiz36m(miktar)
                    bakiye += miktar
                    if money == 1:
                        print(f"{lang["your_balance"]} {bakiye:.2f}₺")
                    elif money == 2:
                        print(f"{lang["your_balance"]} {bakiye:.2f}$")
                    elif money == 3:
                        print(f"{lang["your_balance"]} {bakiye:.2f}€")
                else:
                    print(f"{lang["invalid_choice"]}")
            elif islem == 4:

                while True:
                    islem = int(input(f"{lang["kredi_menu"]}"))

                    if islem == 1:
                        if money == 1:
                            print(kredisorgu(username))
                        elif money == 2:
                            print(kredisorguusd(username))
                        elif money == 3:
                            print(kredisorgueur(username))
                    elif islem == 2:
                        if kredi != 0:
                            print(f"{lang["no_kredi"]}")
                            continue
                        else:
                            kredial(username)
                            if money == 1:
                                u = search_username(username)
                                bakiye = u[5]
                            elif money == 2:
                                ud = search_userdolar(username)
                                bakiye = ud[4]
                            elif money == 3:
                                ue = search_usereur(username)
                                bakiye = ue[4]
                    elif islem == 3:
                        paykredi(username)
                        if money == 1:
                            u = search_username(username)
                            bakiye = u[5]
                        elif money == 2:
                            ud = search_userdolar(username)
                            bakiye = ud[4]
                        elif money == 3:
                            ue = search_usereur(username)
                            bakiye = ue[4]
                    elif islem == 0:
                        break
                    else:
                        print(f"{lang["invalid_operation"]}")
            elif islem == 5:
                while True:
                    money_transfer(username)
                    if money == 1:
                        u = search_username(username)
                        bakiye = u[5]
                        print(f"{lang["your_balance"]} {bakiye}₺")
                    elif money == 2:
                        ud = search_userdolar(username)
                        bakiye = ud[4]
                        print(f"{lang["your_balance"]} {bakiye}$")
                    elif money == 3:
                        ue = search_usereur(username)
                        bakiye = ue[4]
                        print(f"{lang["your_balance"]} {bakiye}€")
                    sor = input(f"{lang["ask"]}")
                    sor = sor.upper()
                    if sor == f"{lang["h"]}":
                        break
            elif islem == 6:
                kumar(username)
                if money == 1:
                    u = search_username(username)
                    bakiye = u[5]
                elif money == 2:
                    ud = search_userdolar(username)
                    bakiye = ud[4]
                elif money == 3:
                    ue = search_usereur(username)
                    bakiye = ue[4]

            elif islem == 11:
                return para_islemleri(username)

            elif islem == 7:
                dovizislem = int(input(f"""
                            {lang["doviz_menu"]}
                            {lang["menu_exit"]}
                                    :"""))
                if dovizislem == 1:
                    dovizinput = int(input(f"""
                            {lang["dolaracc"]}
                            {lang["euracc"]}
                            {lang["menu_exit"]}                           
                                  :"""))
                    if dovizinput == 1:
                        ud = search_userdolar(username)
                        if ud is None:
                            dolar()
                            dolaruser(name, surname, username)
                        else:
                            print(f"{lang["alreadyacc"]}")
                            break
                    elif dovizinput == 2:
                        ue = search_usereur(username)
                        if ue is None:
                            euro()
                            euruser(name, surname, username)
                        else:
                            print(f"{lang["alreadyacc"]}")
                            break

                    elif dovizinput == 0:
                        break
                    else:
                        print(f"{lang["invalid_choice"]}")

                else:
                    print(f"{lang["invalid_choice"]}")
            elif islem == 8:
                u = search_username(username)
                ud = search_userdolar(username)
                ue = search_usereur(username)
                tlbakiye = u[5]
                if ud is None:
                    dolar_bakiye = 0.0
                else:
                    dolar_bakiye = ud[4]
                if ue is None:
                    euro_bakiye = 0.0
                else:
                    euro_bakiye = ue[4]
                while True:
                    parabirimi = input(f"{lang["choicedelete"]}")
                    parabirimi = parabirimi.lower()
                    if parabirimi == "dolar" or parabirimi == "euro":
                        break
                    else:
                        print(f"{lang["yanlistus"]}")
                        continue
                print(f"{lang["tlkarşılık"]}")
                if parabirimi == "dolar":
                    tlbakiye += dolar_bakiye * dolardovizfiyat()
                    update_balance(username, tlbakiye)
                elif parabirimi == "euro":
                    tlbakiye += euro_bakiye * eurdovizfiyat()
                    update_balance(username, tlbakiye)
                delete_acc(username, parabirimi)
                print(f"{lang["başarılısilme"]}")
                return para_islemleri(username)

            elif islem == 9:
                while True:
                    newpass = input(f"{lang["newPass"]}")
                    newpasscheck = input(f"{lang["newPassCheck"]}")
                    if newpass == newpasscheck:
                        upd_password(username,newpass)
                        print(f"{"secure"}")
                        return kullanici_girisi()
                        break
                    else:
                        print(f"{lang["parolauyuşmuyor"]}")
                        continue


            else:
                print(f"{lang["invalid_choice"]}")
            if money == 1:
                update_balance(username, bakiye)
            elif money == 2:
                update_balanceusd(username, bakiye)
            elif money == 3:
                update_balanceeur(username, bakiye)
        except ValueError:
            print(f"{lang["b"]}")
    return bakiye



def sorgud(username):
    ud = search_userdolar(username)
    if ud is None:
        return False
    else:
        return True


def sorgueur(username):
    ue = search_usereur(username)
    if ue is None:
        return False
    else:
        return True


def kullanici_girisi():
    lang = get_dil()
    username = input(f"{lang["enter_username"]} ")
    password = input(f"{lang["enter_password"]} ")
    u = search_username(username)
    ud = search_userdolar(username)
    ue = search_usereur(username)

    if u is None:
        print(f"{lang["login_failed"]}")
        return

    if password == u[4]:
        print(f"{lang["login_success"]} {username}.")
        bakiye = u[5]
        if sorgud(username):
            usdbakiye = ud[4]
            print(f"{lang["your_balance"]} {usdbakiye:.2f}$")
        else:
            print(f"{lang["usdAccNotFound"]}")
        if sorgueur(username):
            eurbakiye = ue[4]
            print(f"{lang["your_balance"]} {eurbakiye:.2f}€")
        else:
            print(f"{lang["eurAccNotFound"]}")
        print(f"{lang["your_balance"]} {bakiye:.2f}₺")
        para_islemleri(username)
    else:
        print(f"{lang['login_failed']}")


def kullanici_kayit():
    lang = get_dil()
    name = input(f"{lang["name"]}")
    surname = input(f"{lang["surname"]}")
    username = input(f"{lang["enter_username"]} ")
    u = search_username(username)
    if u is not None:
        print(f"{lang["username_taken"]}")
        return kullanici_kayit()

    password = input(f"{lang["enter_password"]} ")

    insert(name, surname, username, password, 0)
    print(f"{lang["registration_success"]} {username}.")
    print(f"{lang["c"]}")
    print(f"{lang["your_balance"]} 0 ₺ dir.")
    print(f"{lang["deposit_required"]}")

    kullanici_girisi()





def ana_menu():
    while True:
        dil = getlangnumber()
        lang = get_dil()
        try:
            islem = int(input(f"""{lang["welcome_message"]} 
                                    {lang["date"]} {date.strftime(f" %d %B %Y %A {lang["time"]} %H.%M")}
                                    {lang["login"]}
                                    {lang["register"]}
                                    {lang["toggle_language"]}
                                    {lang["italian"]}
                                    {lang["german"]}
                                    {lang["turk"]}
                                    {lang["logout"]}
                                    :"""))
            if islem == 1:
                kullanici_girisi()
            elif islem == 2:
                kullanici_kayit()
            elif islem == 3:
                if dil == 2:
                    print(f"{lang["k"]}")
                    continue
                else:
                    set_dil(2)
                    locale.setlocale(locale.LC_ALL, 'en_EN')

            elif islem == 4:
                if dil == 3:
                    print(f"{lang["k"]}")
                    continue
                else:
                    set_dil(3)
                    locale.setlocale(locale.LC_ALL, 'it_IT')

            elif islem == 5:
                if dil == 4:
                    print(f"{lang["k"]}")
                    continue
                else:
                    set_dil(4)
                    locale.setlocale(locale.LC_ALL, 'de_DE')
            elif islem == 6:
                if dil == 1:
                    print(f"{lang["k"]}")
                    continue
                else:
                    set_dil(1)
                    locale.setlocale(locale.LC_ALL, '')
            elif islem == 0:
                print(f"{lang["d"]}")
                break
            else:
                print(f"{lang["e"]}")
        except ValueError:
            print(f"{lang["b"]}")


ana_menu()





