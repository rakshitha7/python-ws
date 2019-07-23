#dictionary

names =["pkm","aln","pvr","pkm","aln","gln","nvr","pvr","km","vp","cs","mcs"]

c_name ={ }
for name in names:
    if c_name.get(name)==None:
        c_name[name]=1
    else:
        c_name[name]+=1
print(c_name)