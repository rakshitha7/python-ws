

num = int(input("enter the numvber"))
is_prime=True
if num < 2:
    is_prime = False
else:
    for i in rang(2,num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime")