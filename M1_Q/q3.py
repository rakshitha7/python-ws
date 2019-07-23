'''3.	Write a program to accept 2 different numbers from the user and print all the prime numbers between these 2 numbers.'''

n1=int(input("enter the number n1"))
n2=int(input("enter the number n2"))
for i in range(n1,n2+1):
    is_prime=True
    if i < 2:
        is_prime = False
    else:
        for j in range(2,i// 2 + 1):
            if i % j == 0:
                is_prime = False
                break
    if is_prime:
        print(f"{i} ")
    
    