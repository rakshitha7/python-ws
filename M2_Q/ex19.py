data = "rajesh,krish,anish,aman,ramesh,manoj"

x=list(map(lambda x :x.capitalize(),data.split(",")))
print(list(filter(lambda x:x.startswith("A"),x)))

#to filter the names that start with A