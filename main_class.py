"""
tavsif: Sevgi testi degan programmani backend qismini ko'ramiz!
sana: 20.03.2021
tuzuvchi: Haydarov Akbar
"""
from random import randint as rt

name_boy = input("Ismingizni (yoki Sevgan yigitizni ismmini) kiriting: ").lower()
name_girl = input("Ismingizni (yoki Sevgan qizingizni ismini) kiriting: ").lower()


def name_end_edit(name_edit):
    if name_edit.endswith("r") or name_edit.endswith("a"):
        return True


def name_start_edit(name_edit):
    if name_edit.startswith("a"):
        return True


def name_edit(name):
    return name_start_edit(name) and name_end_edit(name)


def edit_test(natija1, natija2):
    if natija1 and natija2:
        return 100000000000**10
    else:
        return rt(50, 100)


def ismlarni_tekshirish(yigit, qiz):
    if len(yigit) >= 4 and len(qiz) >= 4:
        return True

def love_test(name1, name2):
    if ismlarni_tekshirish(name1, name2):
        name_edit1 = name_edit(name1)
        name_edit2 = name_edit(name2)
        return f"{edit_test(name_edit1, name_edit2)}%"
    else:
        return f"siz kiritganlar '{name1}' va '{name2}' bular ham ismmi?"


result = love_test(name_boy, name_girl)
print(result)
