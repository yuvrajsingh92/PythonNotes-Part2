
# ! What is inheritance: Inheritance let's a new class(child) automatically reuse the the attribute and methods of the existing class(Parent's)

# class Animals:
#     def eat(self):
#         print("Eating")
#     def sleep(self):
#         print("Sleep")

# class Dog(Animals): # This is how have pass the parent class to the child class
#     def bark(self):
#         print("Woof!")

# dog = Dog()
# dog.eat()
# dog.bark()
# dog.sleep()

# ? Method overloading and overriding
# ? Overiding

# class Animal:
#     def speak(self):
#         print("Animal is Speaking")

# class Dog(Animal):
#     def speak(self):
#         print("Dog is Barking")
# # In this case their is 2 method named as speak and when we make a instance and call method speak which method is going to get called?

# d1 = Dog()
# d1.speak() # Which one is going to display. Ans: Dog is Barking. This is called method overriding

# ! In python their is no concept as method overloading

# .super(): # ? When we want to access the parent method which have the same name as child method name so we use super()."methodname" and if their is no common method name we can just access them normally

# class Animal:
#     def speak(self):
#         print("Animal is speaking")

#     def display(self):
#         print("This is display function")

# class Dog(Animal):
#     def speak(self):
#         # if we try 
#         # self.speak() # This will make an infinte loop
#         super().speak()
#         self.display() # This is display function
#         print("Dog is Barking")

# d1 = Dog()
# d1.speak() # Animal is speaking Dog is Barking

# ? Using super in __init__

# class Vehicle:
#     def __init__(self,brand:str):
#         print("This is Vehicle Construtor")
#         self.brand = brand

# class Car(Vehicle):
#     def __init__(self,brand:str,fuel:str):
#         print("This is car constructor")
#         super().__init__(brand)
#         self.fuel = fuel

#     def display(self):
#         print(f"This is {self.brand} car and the fuel is {self.fuel} type")

# car = Car("Hoyaa","Cum")
# car.display()


# ! Types of inheritance: Single Inheritance, MultiLevel Inheritance, Hierarchical Inheritance, Multiple Inheritance

# ? Multilevel Inheritance: Multilevel inheritance is like grandparents, parents and child

# class Animal:
#     def breathe(self):
#         print("Breathing....")

# class Mammal(Animal):
#     def feed_young(self):
#         print("Feeding....")

# class Dog(Mammal):
#     def Bark(self):
#         print("Barking")

# d1 = Dog()
# d1.breathe()
# d1.feed_young()
# d1.Bark() # ? Example of multilevel inheritance

# ? Multiple Inheritance: One child can have both the parents attribute and methods

# class Fly:
#     def can_fly(self):
#         print("Flyinh...")

# class Swim:
#     def can_swim(self):
#         print("Swiming...")

# class Puffin(Fly,Swim):
#     def both(self,bird:str):
#         self.bird = bird
#         print(f"{self.bird} can littraly fly and swim")


# puff = Puffin()
# puff.both("Puffin")


# ? Hierarchical Inheritance: Mulitple child class can inheritance single parent class

# class Animal:
#     def __init__(self,name:str):
#         self.name = name

#     def breathe(self):
#         print(f"{self.name} is breathing")

# class Dog(Animal):
#     def bark(self):
#         print("Woof!")

# class Cat(Animal):
#     def meow(self):
#         print("Meow!")

# class Cow(Animal):
#     def moo(self):
#         print("Mooo!")

# dog = Dog("Sheru")
# cat = Cat("Bagira")
# cow = Cow("Gauri")

# # All Inherit animals can breathe and can access 
# dog.breathe()
# cat.breathe()
# cow.breathe()

# ? Diamond problem Or MRO(Method Resolution Order): Below is the problem can you tell me what will be the output

# class A:
#     def hello(self):
#         print("Hello From A")

# class B(A):
#     def hello(self):
#         print("Hello From B")

# class C(A):
#     def hello(self):
#         print("Hello From C")

# class D(B,C):
#     pass

# hello = D()
# hello.hello() # What will be the output?: The Output will be : "Hello From B" Because class B have pass first so it will have more prorty. And if we have passed class D(C,B) Then the ouput would have been "Hello From C"

# print(D.__mro__) # From this we can get to know which have highest priorty
# ? (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

