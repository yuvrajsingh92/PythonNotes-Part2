
# ! What is dunder methods: Dunder methods means double underscore, These are special methods python calls automatically for build-in-operations

# ? __str__ 

# class Point:
#     def __init__(self,x:int,y:int):
#         self.x = x
#         self.y = y

#     def __str__(self) ->str :
#         return (f"Point are {self.x} and {self.y}")
# p = Point(3,4)
# print(p) # ? It will return object memory address <__main__.Point object at 0x0000029FDFCB9D00>. Here __str__ methods comes in place and it we try to print now thier will be no memory address coming and we have to always return


# ? __eq__: When we have to compare two object we use this methods

# class Money:
#     def __init__(self,amount):
#         self.amount = amount

#     def __eq__(self, other): # In place of other we can take anything but we prefare other because object one goes to self and second one goes to another object to we prefare other
#         return self.amount == other.amount

# m1 = Money(100)
# m2 = Money(200)
# print(m1 == m2) # False 

# ? __lt__: Is used to compare two objects which one is bigger

# class Money:
#     def __init__(self,amount:int):
#         self.amount = amount

#     def __eq__(self, other):
#         return self.amount == other.amount

#     def __lt__(self, other):
#         return self.amount < other.amount

# m1 = Money(100)
# m2 = Money(300)
# print(m1 < m2)

# ? __le__: is used to compare two objects which one is greater or equal

# class Money:
#     def __init__(self,amount):
#         self.amount = amount

#     def __le__(self, other):
#         return self.amount <= other.amount

# m1 = Money(200)
# m2 = Money(100)
# # print(m1 <= m2) # True
# print(m1 <= m2) # False

# ? same as __gt__ and __ge__: used to compare two object 

# class Amount:
#     def __init__(self,amount:int):
#         self.amount = amount

#     def __gt__(self, other):
#         return self.amount > other.amount

# a1 = Amount(1000)
# a2 = Amount(100)
# print(a1 > a2) # True
# print(a1 < a2) # False

# ? __ge__
# class Amount:
#     def __init__(self,amount:int):
#         self.amount = amount

#     def __ge__(self, other):
#         return self.amount >= other.amount

# a1 = Amount(1000)
# a2 = Amount(100)
# print(a1 >= a2) # True
# print(a1 <= a2) # False

# ! Here are some dunder methods use to do operation which number __add__, __sub__, __mul__

# class Distance:
#     def __init__(self,km:int):
#         self.km = km

#     def __add__(self, other):
#         return self.km + other.km

#     def __sub__(self, other):
#         return self.km - other.km

#     def __mul__(self, other):
#         return self.km * other.km

# d1 = Distance(10) 
# d2 = Distance(2)
# print(d1+d2) # 12
# print(d1-d2) # 8
# print(d1*d2) # 20

