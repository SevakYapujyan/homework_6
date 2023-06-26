
# num = int(input("write num --->>"))


def print_p(num):
    ls_1 = []
    ls_2 = []
    for i in range(2,num+2):
        for j in range(1,i):
            ls_1.append(j)
        ls_2.append(ls_1)
        ls_1 = []
    return ls_2
print(print_p(5))



