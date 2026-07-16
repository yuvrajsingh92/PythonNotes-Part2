
# ! What is abstraction?: Abstraction is the fourth pillar of Oops. It works as hidding how something works and exposing only what it does

# ? Real World example or analog is: When we press the brack or when we on the car the work which is going on behind we don't need to think about is called abstaction

# code Example

# class Shape:
#     def area(self):
#         pass

#     def parameter(self):
#         pass

# class Rectangle(Shape):
#     def area(self):
#         pass

#     def parameter(self):
#         pass

# rect = Rectangle() # This code will run but in abstraction it does work this way


# ? Example of abstract class

# from abc import ABC,abstractmethod

# class Shapes:
#     @abstractmethod # We have to pass it. so it's compalsory to make the method for child class
#     def area(self):
#         pass
#     @abstractmethod
#     def parameter(self):
#         pass

# class Rectangle(Shapes):
#     def __init__(self,l:int | float, b:int|float):
#         self.length = l
#         self.breath = b

#     def area(self):
#         return self.length * self.breath

#     def parameter(self):
#         return 2 * (self.length + self.breath)

# rect = Rectangle(10,20)
# print(rect.area())
# print(rect.parameter())

