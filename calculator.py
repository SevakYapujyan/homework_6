
num_1 = 0
operator = ""
num_2 = 0

def calculator (num_1,operator,num_2):
    
    num_1 = int(input("if you want to exit write 'exit' \nwrite first number--> "))

    operator = input("if you want to exit write 'exit' \nchoose an operator (+ - * /) --->> ")

    num_2 = int(input("if you want to exit write 'exit' \nwrite second number--> "))

    if operator == "+":
        out_num = num_1 + num_2
    elif operator == "-":
        out_num = num_1 - num_2
    elif operator == "*":
        out_num = num_1 * num_2
    elif operator == "/":
        out_num = num_1 / num_2
    else:
        print("you have a bug, try again")

    print(out_num)

while num_1 or operator or num_2 != "exit":
    calculator(num_1,operator,num_2)


