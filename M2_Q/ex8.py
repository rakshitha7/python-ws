data="rajesh,aman,raj,suresh,anish,vinish,ankith"

names=data.lower().split(",")
print(names)

ls=[]
for i in  names:
    if i.startswith("a") or i.endswith("h"):
        ls.append(i)
ls.sort()
print(ls)

