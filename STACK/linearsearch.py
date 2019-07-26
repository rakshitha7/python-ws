def searchLinear(lst,ele):
    index=0
    for i in lst:
        if i==ele:
            return index
        index +=1
    return -1

ele=69
res=searchLinear([1,5,1,6,1,2,3,],ele)
if res == -1:
    print(f"{ele} is not found")
else:
    print(f"{ele} is found at :{res}")