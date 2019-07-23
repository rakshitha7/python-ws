'''5.	Write a program to print the Fibonacci series up to the number 34. 
(Example: 0,1,1,2,3,5,8,13,… The Fibonacci Series always starts with 0 and 1, the numbers that follow are arrived at by adding the 2 previous numbers.)
'''

t1=0
t2=1
print (f"{t1}")
print(f"{t2}")
while True:
   
    nextterm = t1 + t2
    t1=t2
    t2=nextterm
    print(f"{nextterm}")
    if(nextterm==34):
        break
