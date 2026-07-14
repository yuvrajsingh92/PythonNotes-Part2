
# ! What is encapsulation: Encapsulation is One of the Oops pillar. The purpose of encapsulation is practic of binding data and methods together, and resitricting direct access

# ? Encapsulation prevents accidental modification of important data
# ? Enforce rules through methods such as validations and logging
# ? Keeps internal through a clean interface 

# ! Their are three type of encapsulation
"""
1) Public: Anyone can access it
2) Protected: Intented for internal use. but accessible 
3) Private: Stroge internal with name mangling
"""

# ? Public Example: We can Access and modifiy it 

# class Student:
#     def __init__(self, name:str, age:int):
#         self.name  = name
#         self.age = age

# s1 = Student("Yuvraj Singh",21)
# print(s1.name) # Yuvraj Singh
# s1.age = 22
# print(s1.age) # 22 

# ? Protected Example:Is been made by using single underscore prefix is a conventional singnaling

# class Bank:
#     def __init__(self, name:str, balance:float|int):
#         self.name = name
#         self._balance = balance

#     def get_balance(self):
#         return self._balance

# ah = Bank("Ayush",1000)
# print(ah.name)
# print(ah.get_balance()) # We can still access it. it just convention

# ? Private Example: it's been made by using double underscore prefix. prefix triggers name mangling - Python actually changes the attribute name behind the scencs

# class Bank:
#     def __init__(self, owner:str, Balance: float | int):
#         self.owner = owner
#         self.__Balance = Balance 

#     def deposite_amount(self,amount:int):
#         if amount < 0:
#             print("Invalid About")
#         else:
#             self.__Balance += amount

#     def get_balance(self):
#         return self.__Balance

# AH = Bank("Ayush Singh",100000)
# print(AH.owner) # name
# print(AH.get_balance())
# AH.deposite_amount(1000)
# print(AH.get_balance())
# print(AH.__Balance) # Error because it is private
# print(AH._Bank__Balance) # ? We can access it by put underscore and then putting class name and then putting the attribute

# ? As we can see that we can access data even when we have make it private, because in python their is no thing as strick data hyding
# print(AH._Bank__Balance) # And this is called as name mangling

# ! getter and setter

# class Student:
#     def __init__(self,name:str):
#         self.__name = name

#     # getter
#     def getter_name(self):
#         return self.__name

#     # setter
#     def setter_name(self,new_name:str):
#         self.__name = new_name

# s1 = Student("Ayush")
# print(s1.getter_name())
# s1.setter_name("Yuvraj Singh")
# print(s1.getter_name())

# ? Getter and setters using new way

# class School:
#     def __init__(self,name):
#         self.__name = name

#     @property
#     def getter(self):
#         return self.__name

#     # To create a setter we have to do like this
#     @getter.setter # ? we have to put @ and the getter method name then . then the name you want to put
#     def setter(self,new_name:str):
#         self.__name = new_name

# s1 = School("Yuvraj Singh")
# print(s1.getter) # ? See when we use @property we don't need to call the method like the normal way. it's like a data hyding when we call it like a normal variable but calling a method

# s1.setter = "Ayush Singh"
# print(s1.getter)

