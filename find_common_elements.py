
def find_common_elements (ls,ls_1):
    for i in ls:
        for j in ls_1:
            if i == j: 
                print(i)
            else:
                print("there are no elements between two input lists")

print(find_common_elements([],[]))




