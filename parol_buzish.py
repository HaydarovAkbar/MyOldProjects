user_parol = input("buziladigan parolni kiriting: ").lower()
from Kalit_suzlar import alphabet
from random import choice

count = 0
tahmin = ""
while tahmin != user_parol:
    tahmin = ""
    for i in range(len(user_parol)):
        tahmin += choice(alphabet)
    print(tahmin)
    count += 1
print(count)