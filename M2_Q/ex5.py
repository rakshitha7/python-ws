import random as rn 
lst=[]

for i in range(1,100):

    lst.append(rn.randint(1,1000))
st=[]
for j in  lst:
    if j % 3 == 0 and j % 6 ==0 and j % 9 != 0:
        st.append(j)
print(st)