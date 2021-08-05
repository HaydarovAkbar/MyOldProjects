"""
tavsif: Sezer shifrlashi 'yani alfabetdagi harflarni bitta keyingisiga almashtish'
sana: 23-03-2021
tuzuvchi: Haydarov Akbar
"""
from Kalit_suzlar import alphabet as alp

user_kod = input("Kodni kiriting:").lower()


def control_item(item):
    """harfni olib keyngi harfni qaytaradigan funksiya"""
    idx_item = alp.index(item)
    return alp[idx_item + 1]


def main(user_kod):
    """malumotni olib shifrlab beradigan funksiya"""
    result = ""
    for item in user_kod:
        result += control_item(item)
    return result


print(main(user_kod))
