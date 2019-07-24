# object oriented concept
#class


class Car:


    def __init__(self,regno,no_gears):
        self.regno=regno
        self.no_gears=no_gears
        self.is_started=False
        self.c_gear = 0

    def start(self):
        if self.is_started:
            print(f"car with regno {self.regno} already started....")
        else:
             print(f"car with regno {self.regno} started....")
             self.is_started=True

    def stop(self):
        if self.is_started:
            print(f"{self.regno} stoped......")
            self.is_started=False
        else:
            print(f"{self.regno} already stoped......")
            
    def change_gear(self):
        if self.is_started:
            if self.c_gear < self.no_gears:
                self.c_gear += 1
                print(f"{self.regno} changed gear...{self.c_gear}..")
                
            else:
                print(f"{self.regno} already raeched top  gear you cannot change the gear....{self.c_gear}.")    
        else:
             print(f"{self.regno} stoped...yuo cannot change the gear...")


    def showInFo(self):
        print(f"car with regno {self.regno} -no_gear: {self.no_gears} -gear_status:{self.c_gear}")