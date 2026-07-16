
# ! Polymorphism: Is the 3 Pillar of oops. Is more like method overriding
# Example:

class Shapes:
    def area(self):
        return 0

class Rectangle(Shapes): # Inherting Shapes class
    def __init__(self,w,h):
        self.w,self.h = w,h

    def area(self):
        return self.w * self.h

class Circle(Shapes):
    def __init__(self,r):
        self.r = r

    def area(self):
        return 3.14 * self.r**2

shapes = [Rectangle(3,4), Circle(5),Rectangle(2,6)]  # Perfact Example of polymorphism
for i in shapes:
    print(i.area())