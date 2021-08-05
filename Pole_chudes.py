from Kalit_suzlar import malumot
from random import choice

"""
tavsif: Pole chudes dasturi sizga qiziqarli savollar beradi uni topishga harakat qilib kurasiz
sana: 22:03:2021
tuzuvchi: Haydarov Akbar
"""


def control_letter(letter, block, letters):
    """user kiritgan harf to'ri bo'lsa uzini aks holda - ni qaytaradi"""
    result = ""
    for item in block:
        if item in letters:
            result += item
        else:
            result += "-"
    return result


def control_result(letters, user_letter, block):
    """user kiritgan harf avval ham kiritganmidi yoki yuq shuni tekshiradi"""
    if user_letter in letters:
        print(f"'{user_letter}' buni avval kiritgansiz etiborli bo'ling")
    elif user_letter in block:
        print("<<<To'g'ri>>>")
    else:
        print("<<<Xato>>>")


def len_1(user):
    """user kiritgan harfni tekshiradigan funksiya"""
    if len(user) == 1:
        return user
    else:
        print("iltimos bitta harf kiriting"
              " javobini bilsangiz boshida kiritish kerak edi!")
        return user[0]


def user_letters(block, urinishlar_soni):
    """bu funksiya user kiritgan harflar to'ri bolsa yiigb boradigan funksiya"""
    letters = ""
    urinishlar_soni += 4
    while urinishlar_soni > 0:
        try:
            user_letter_1 = input("Harf kiriting> >").lower()
            user_letter = len_1(user_letter_1)
            control_result(letters, user_letter, block)
            letters += user_letter
            javob = control_letter(user_letter, block, letters)
            urinishlar_soni -= 1
            print(f"{javob.capitalize()}\n")
            if javob == block: # Javob agar to'ri bo'lsa shu yerda natija chiqadi
                print(f"Barakalla siz '''{block}''' ni {len(block) + 4 - urinishlar_soni} tada topdingiz")
                break
            else:
                print(f"Sizda yana {urinishlar_soni} urinish bor")
        except:
            print("?")


def choice_func(dicts):
    """bu funksiya dictdan ixtiyoriy elementni olib beradi"""
    key = choice(list(dicts.keys()))
    return key


def len_answer(block):
    """javob necha xonalli ekanini aniqlab beruvchi funksiya"""
    answer_len = len(block)
    print(f"savolni javobi {answer_len} xonali so'z shunga etibor bering")
    return answer_len


def one_urinish(block):
    """user javobni bilsa bir urinishda kiritadigan funksiya"""
    user_javob = input("urinib kuring: ").lower()
    if user_javob == block:
        print("Shunchaki qoyil")
        return 1
    else:
        print("O'xshamadiyu")
        return 0


def main_func(user):
    """asosiy funksiyalardan biri"""
    block = choice_func(user)
    print(malumot.get(block, "sorry") + "ni toping?")
    urinishlar_soni = len_answer(block)
    a = input(f"sizda jami {urinishlar_soni + 4} ta urinish bor"
              f"\nAgar so'zni bilsangiz bittada kiritish uchun 1 ni kiriting")
    if a == "1":
        one_urinish1 = one_urinish(block)
        if one_urinish1 == 1:
            return 1
        else:
            return 0
    else:
        user_letters(block, urinishlar_soni)


def like_func(count):
    """dasturni baholovchi funksiya"""
    like = input("dastur sizga yoqdimi yoki yuq (1/0)")
    if like == "1":
        print(f"Thanks {count} marta o'ynadiz")
    else:
        print(f"Ok {count} marta o'ynadiz")


def while_func(malumot):
    """bu funksiya yana o'ynamoqchi bulsa takrorlab beradi"""
    count = 0
    while True:
        count += 1
        a = main_func(malumot)
        again = input("yana o'ynaymizmi")
        if again in ["yes", "ha", "1", "da", "albatta", "xop", "mayli"] or (
                a == 1 and again not in ["no", "0", "kerakmas", "yo", "yuq"]):
            pass
        else:
            like_func(count)
            break


while_func(malumot)