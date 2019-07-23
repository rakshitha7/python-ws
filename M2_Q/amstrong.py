def amstrong_num(num):
    res=0
    num1=num
    while num!=0:
        r=num%10
        res=res+r**3
        num=num//10
    return num1==res

inp=int(input("enter the number"))
if(amstrong_num(inp)):
    print(f"given number {inp} is a amstrong number")
else:
     print(f"given number {inp} is a not amstrong number")
