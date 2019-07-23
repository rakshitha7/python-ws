Cricket=["PKM","ALN","GLN","NVR","PVR","KM","VP","CS","MCS"]
Football=["PKM","ALN","RMZ","CS","MCS"]
Badminton=["PKM","ALN","NV","KM","RMV"]

name= []
player = []
player.extend(Cricket)
player.extend(Football)
player.extend(Badminton)

for i in player:
    if  not i in name:
        name.append(i)
print(name)