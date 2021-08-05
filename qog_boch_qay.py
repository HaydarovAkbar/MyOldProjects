"""
tavsif: tosh,qaychi,qog'oz uyinini esingdami shu
sana: 23-03-2021
tavsif: Haydarov Akbar
"""
from Kalit_suzlar import q_b_q as qb
from random import choice
from math import pi


def qogoz_f(nums, komp):
    if komp == "qogoz" and nums != "qogoz":
        if nums == "qaychi":
            return True
        else:
            return False
    elif komp != "qogoz" and nums == "qogoz":
        if komp == "qaychi":
            return False
        else:
            return True
    else:
        return "xato"


def tosh_f(nums, komp):
    if komp == "tosh" and nums != "tosh":
        if nums == "qogoz":
            return True
        else:
            return False
    elif komp != "tosh" and nums == "tosh":
        if komp == "qogoz":
            return False
        else:
            return True
    else:
        return "xato"


def qaychi_f(nums, komp):
    if komp == "qaychi" and nums != "qaychi":
        if nums == "tosh":
            return True
        else:
            return False
    elif komp != "qaychi" and nums == "qaychi":
        if komp == "qogoz":
            return False
        else:
            return True
    else:
        return "xato"


def komp_qushish(komp_hisob):
    komp_hisob += 1
    return komp_hisob


def user_qushish(user_hisob):
    user_hisob += 1
    return user_hisob


def main(nums, komp, user_hisob, komp_hisob):
    if nums == "qogoz" or komp == "qogoz":
        farq = qogoz_f(nums, komp)
        if farq == True:
            print(f"Siz yutdingiz\nmanda {komp}\n")
            user_hisob = user_qushish(user_hisob)
        elif farq == False:
            print(f"yutqazdingiz\nmanda {komp}\n")
            komp_hisob = komp_qushish(komp_hisob)
        else:
            print("Durrang\n")
    elif nums == "tosh" or komp == "tosh":
        farq = tosh_f(nums, komp)
        if farq == True:
            print(f"Siz yutdingiz\nmanda {komp}\n")
            user_hisob = user_qushish(user_hisob)
        elif farq == False:
            print(f"yutqazdingiz\nmanda {komp}\n")
            komp_hisob = komp_qushish(komp_hisob)
        else:
            print("Durrang\n")
    else:
        farq = qaychi_f(nums, komp)
        if farq == True:
            print(f"Siz yutdinzgiz\nmanda {komp}\n")
            user_hisob = user_qushish(user_hisob)
        elif farq == False:
            print(f"yutqazdingiz\nmanda {komp}\n")
            komp_hisob = komp_qushish(komp_hisob)
        else:
            print("Durrang\n")
    return [user_hisob, komp_hisob]


if __name__ == '__main__':
    print("Keling o'yin o'ynaymiz (tosh,qaychi,qogoz) dan birini tanlaysiz\n"
          "o'yindan chiqish uchun 0 ni kiriting")
    user_hisob = 0
    komp_hisob = 0
    while True:
        user = input("kiriting >>")
        komp = choice(qb)
        if user == "0":
            print("Rahmat")
            break
        if user not in qb:
            print("sorry")
            continue
        result = main(user, komp, user_hisob, komp_hisob)
        user_hisob, komp_hisob = result[0], result[1]
        print(f"achkolar: sizda <<< {result[0]} >>> maniki >>> {result[1]} <<<")
