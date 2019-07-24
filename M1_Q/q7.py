'''7.Write a program to accept a number from the user and determine the sum of digits of that number. Repeat the operation until the sum gets to be a single digit number.'''

sum = 0
count = 0
def find_sum(num):
    sum = 0
    while num > 0 or sum > 9:
        if num == 0:
            num = sum 
            sum = 0
        sum += num % 10
        num = num // 10
    return sum
num = int(input("enter the number:"))
res = find_sum(num)
print(res)
