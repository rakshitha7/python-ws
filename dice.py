'''program for dice'''
import random as rn 
num =rn.randint(1,6)
count=0
while True:
    inp_num=int(input("enter the number"))
    if(inp_num==num):
        count+=1
        print(f"youguessed number in {count} attemp")
        break
    elif inp_num<num:
        print("guessed number  is less than actual number")
        count+=1
    else:
        print("guessed number is greater than actual number")
        count+=1
    if (count==3):
        print("better luck next time")
        break
