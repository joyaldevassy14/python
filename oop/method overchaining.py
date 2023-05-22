class Vechicle:

    def drive(self):
        print("vechicle os driving")

class Truck(Vechicle):

    def color(self):
        print("the color is red")
        return self


class Car(Truck,Vechicle):

    def stop(self):
        print("car is stopped")
        return self #for overiding
    def drive(self):
        print("car is driving")#overiding
        return self #for overiding


vc=Vechicle()
tc=Truck()
cc=Car()

vc.drive()
tc.drive()#inheritance
cc.color().drive()





