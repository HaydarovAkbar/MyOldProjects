print("0.5 stavkali ishga beriladigan ustama summasi aniqlovchi dastur tuzing")
savol = "To'liq stavkali ishning oylik maoshini kiriting "
savol += "(dastur  to'xtatish uchun 'exit' yoki 'stop' ni kiriting):"
ustama_savol = "Necha % ustama olasiz: "

def ustamani_ober(ustama,oylik):
    half_stavka_price = float(oylik) / 2
    ustama_summa = half_stavka_price * int(ustama) / 100
    return ustama_summa

def main_func(savol,ustama_s):
    "Bu funksiya asosiy birlashtiruvchi funksiya buladi"
    while True:
        ustama_foiz = input(ustama_s).lower()
        oylik_price = input(savol).lower()
        if ustama_foiz in ["exit","stop"] and oylik_price in ["exit","stop"]:
            print("Dastur tugadi!")
            break
        try:
            if float(oylik_price) < 0:
                continue
            else:
                result = ustamani_ober(ustama_foiz,oylik_price)
                print(result)
        except:
            print("Xato kiritdingiz!")
main_func(savol,ustama_savol)
s = input("satrni kiriting: ")
number = int(input("sonni kiriting: "))

def main_func(s, number):
    result = [""] * number
    s_index = 0
    uzgartiruvchi = 1
    for item in range(len(s)):
        result[s_index] = result[s_index] + s[item]
        if s_index < number - 1 and uzgartiruvchi == 1:
            s_index += 1
        elif s_index > 0 and uzgartiruvchi == - 1:
            s_index -= 1
        else:
            uzgartiruvchi *= -1
            s_index += uzgartiruvchi
    print(result)
    return "".join(result)


print(main_func(s, number))
