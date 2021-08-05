user_kod = input("ma'lumotni kiritavering: ")
user_list = user_kod.split()
class Exercise:
    def __init__(self,user_list):
        self.user_list = user_list

    def math_func(self,item):
        if self.user_list[item-1] == "+":
            return int(self.user_list[item])
        else:
            return -int(self.user_list[item])

    def user_list_func(self):
        sum_result = int(self.user_list[0])
        for item in range(2,len(self.user_list),2):
            sum_result += Exercise.math_func(item)
        return sum_result
result = Exercise(user_list)
print(result.user_list_func())
