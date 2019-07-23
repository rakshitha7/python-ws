'''4.	Write a program to accept a number “n” from the user; then display the sum of the following series:
1/23+1/33+1/43 + ……+1/n3'''


n=int(input("enter the value of n"))
sum=0
for i in range (2,n+1):
    sum=sum+(1/pow(i,3))

print(f"the sum of series is {sum}")
