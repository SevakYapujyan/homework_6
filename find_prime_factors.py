

def find_prime_factors (num):
    if num <= 0:
        print("bag")
        return []
    div = 2
    ls = []
    while num > 1:
        if num % div == 0 :
            ls.append(div)
            num = num // div
        else:
            div += 1
    return ls    
print(find_prime_factors(289))

