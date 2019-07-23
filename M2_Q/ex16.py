name=input("enter your name")
lst = ['a','e','i','o','u']
c=0
for i in name:
    if i in lst:
        c=c+1
print(c)


#using filter
'''print(len(list(filter(lambda x:x in lst,name))))'''