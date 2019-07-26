def binarysearch(lst,key):
    l=0
    h=len(lst)-1
    while l<=h:
        mid=(l+h)//2
        if lst[mid] == key:
            return mid
        elif  key>lst[mid]:
            l=mid+1
        else:
            h=mid-1
    return -1

ele=6
res=binarysearch([1,2,3,4,5,6,7],ele)
if res == -1:
    print(f"{ele} is not found")
else:
    print(f"{ele} is found at :{res}")