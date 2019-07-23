def get_digits(num):
    temp=num
    a,temp = temp // 1000,temp % 1000
    b,temp = temp // 100,temp % 100
    c,temp = temp // 10,temp % 10
    d,temp = temp // 1,temp % 1
    return a,b,c,d

for i in rangr(1000.10000):
    if sum_digit(i) == 12:

