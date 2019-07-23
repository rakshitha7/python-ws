'''reverse number'''
def reverse_num(num):
    rev=0
    while num !=0 :
        rev=rev*10+num% 10
        num//=10
    return rev

num=int(input("enter the number"))
rev=reverse_num(num)
print(f"reverse of {num} is {rev}")