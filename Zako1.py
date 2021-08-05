class Sanoq:
    """Sanoq sistemasi sinfi"""

    def __init__(self,x):
        self.x = x

    def ikkilikga(self,item):
        s2 = ""
        while item > 1:
            s2 += str(item % 2)
            item = item // 2
        s2 += str(item)
        result = s2[::-1]
        return Sanoq(result)

    def sakkizlikga(self,other):
        s8 = ""
        while other > 7:
            s8 += str(other % 8)
            other //= 8
        s8 += str(other)
        result = s8[::-1]
        return Sanoq(result)

    def ikkilikdan(self,key):
        result = ""
        q = 0
        for item in range(len(key)):
            result += str(oct(int(key[q,q+8])))
            q += 8
        print(result)

son1 = Sanoq(15)
son2 = Sanoq(10001111)
# print(son1.ikkilikga())
# print(son1.sakkizlikga())
print(son2.ikkilikdan("10101010"))