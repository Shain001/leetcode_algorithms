"""
    判断水仙花数， 153 = 1^3 + 5^3 + 3^3 --> True

"""


def temp(num):
    num1 = num//100
    num3 = num % 10
    num2 = ((num-num3) / 10) % 10
    if num1**3 + num2 **3 + num3**3 == num:
        return True
    return False


test = 100
print(temp(test))