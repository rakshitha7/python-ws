'''5. Write a program to add the elements of 2 arrays that are of the same dimension. (Hint: Use
map method.)
Example:
Input:
x = [1,2,3,4]
y = [5,6,7,8]
Output:
z = [6,8,10,12]'''

ls1 = [1,2,3,4]
ls2 = [4,5,6,7]
res = []
for i in range(0,len(ls1)):
    res.append(ls1[i]+ls2[i])
print(res)

#res=list(map(lambda a,b : a + b ,ls1,ls2)