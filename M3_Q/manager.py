from car import Car


car_1= Car("KA013060",5)
car_2= Car("KA013060",6)
car_3= Car("KA013070",4)
car_4= Car("KA013056",8)
car_1.start()
car_2.start()
car_3.start()
car_4.start()

car_1.change_gear()

car_2.change_gear()

car_1.change_gear()

lst=[car_1,car_2,car_3,car_4]

for car in lst:
    car.showInFo()
c=len(list(filter(lambda x:x.is_started and x.c_gear == 0,lst)))
print(c)