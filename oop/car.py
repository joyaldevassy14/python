class Car:
    wheels=4
    def __init__ (self,make,color,year):
        self.make= make
        self.color= color
        self.year= year


    def drive(self):
        print(self.make+"is  car is driving")

    def stop(self):
        print(self.make+" is  car is stopped")

car1=Car("1","2","3")
car2=Car("suzuki","20200","sedan")



print(car1.make)
print(car1.color)
print(car2.year)
print(car1.wheels)
print(Car.wheels)


car1.drive()
car1.stop()



class Car2:
    wheels=4
    def __init__ (self,make,color,year):
        self.make= make
        self.color= color
        self.year= year


    def drive(self):
        print(self.make+"is  car is driving")

    def stop(self):
        print(self.make+" is  car is stopped")

car1=Car2("1","2","3")
car2=Car2("suzuki","20200","sedan")



print(car1.make)
print(car1.color)
print(car2.year)
print(car1.wheels)
print(Car.wheels)


car1.drive()
car1.stop()


class Truck(Car,Car2):

    def __init__ (self,re,re2,re3):
        self.color=re
        self.year=re2
        self.make=re3

    def breaking(self):

        print(self.make+" is breaking")


t1=Truck("1","2","truck")
t1.drive()
t1.breaking()




