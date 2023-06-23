
def find_factorial (int_num):
    if int_num == 0:
        pass
    else:
        num = 1
        while int_num > 0:
            num *= int_num
            int_num -= 1
        return num
print(find_factorial(0))



