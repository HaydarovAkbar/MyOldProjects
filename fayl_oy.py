class Odam():
    """Inson clasi"""
    def __init__(self,boyi,ogirligi,rangi,millat):
        self.boyi = boyi
        self.ogirligi = ogirligi
        self.rangi = rangi
        self.millati = millat

    def get_info(self):
        info = f"Og'irligi:{self.ogirligi}kg, Bo'yi:{self.boyi}sm "
        info += f"Rangi:{self.rangi}, Millati:{self.millati},"
        return info

    def set_boyi(self,new_boy):
        self.boyi = new_boy

    def set_ogirligi(self,new_vazn):
        self.ogirligi = new_vazn

    def __str__(self):
        return f"Og'irlik {self.ogirligi}"
# odam1 = Odam(132,67,"qora","Uzbek")
# odam1.set_boyi(178)
# odam1.set_ogirligi(89)
class Biznesman(Odam):
    """bu BIznesman clasi"""
    def __init__(self,ism,boyi,ogirligi,millati,rangi,yili,maosh):
        super().__init__(self,boyi,ogirligi,millati)
        self.ism = ism
        self.rangi = rangi
        self.yili = yili
        self.maosh = maosh
    def get_info(self):
        info = f"mani ismim {self.ism} mani bo'yim {self.boyi} og'irligim esa {self.ogirligi} millatim"
        info += f"{self.millati}, rangim: {self.rangi} yoshim {self.yili}, oylik maoshim esa {self.maosh}"
        return info
man1 = Biznesman("Akbar",183,75,"Uzbek","Oq",21,"1000$")
print(man1.get_info())