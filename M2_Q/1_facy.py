'''1. Write a program to generate a fancy number for a new vehicle considering the following
constraints:
a. The fancy number should have 4-digits.
b. The sum of these 4-digits should be 12.
c. The 3 rd digit should be equal to the difference between the 1 st and the 2 nd digit.
d. The 4 th digit should be equal to the sum of the 1 st and the 3 rd digit.
The program should be able to generate all the possible 4-digit numbers that meet the above
listed criteria.'''

def sum_digit(num):
    if num < 10:
        return num
    s=0
    while num!=0:
        s+= num %10
        num=num//10
    return s


def get_digits(num):
    temp=num
    a,temp = temp // 1000,temp % 1000
    b,temp = temp // 100,temp % 100
    c,temp = temp // 10,temp % 10
    d,temp = temp // 1,temp % 1
    return a,b,c,d

for i in range(1000,10000):
    if sum_digit(i) == 12:
        a,b,c,d=get_digits(i)
        if a-b == c and a + c ==d:
            print(i)

