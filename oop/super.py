class Shape:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        print(self.length*self.width)
class Square(Shape):
    def __init__(self,length,width):
        super().__init__(length,width)

class Rectangle(Shape):
    def __init__(self,length,width,hypo):
        super().__init__(length,width)
        self.hypo=hypo
    def area(self):
        print(self.length*self.width*self.hypo)
    
s=Square(10,20)
r=Rectangle(10,20,30)


s.area()
r.area()


food=list()
f=1
while f!="quit":
    f=input("Enter the food")
    food.append(f)

print(*food)



food1=list()
while food2:=input("Enter the food you like")!="quit":
    food1.append(food2)
print(food1)