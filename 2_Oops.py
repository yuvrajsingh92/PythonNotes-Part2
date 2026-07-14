
# ! Oops : Oops stand for "Object Oriented programming". oops is a concept in oops their are various concepts

# ! Classes and Objects

# ? How to make an class : we use keyword class and give it a name in camelcase

# class Student:
#     # This variables are called as attributes
#     roll_no = 0
#     name = ""
#     gender = ""
#     age = 0 

# student1 = Student() # This is called as Object or Instance 
# ? but how to give value 

# student1.roll_no = 91
# student1.name = "Yuvraj Singh"
# student1.gender = "Male"
# student1.age = 18
# print(student1.roll_no)
# print(student1.name)
# print(student1.gender)
# print(student1.age)

# Creating another Instance

# student2 =Student()

# student2.roll_no = 331
# student2.name = "Yuvraj Singh"
# student2.gender = "Male"
# student2.age = 21

# print(student2.roll_no)
# print(student2.name)
# print(student2.gender)
# print(student2.age)

# ? Their is so much line of code for this to make it easer we use oops concepts

# class Students:
#     roll_no = 0
#     name = ""
#     Gender = ""
#     Age = 0

#     # ? function inside of class is called "method"
#     def set_details(self,r,n,g,a): # self is a inbuilt keyword special for oops
#         self.roll_no = r
#         self.name = n
#         self.Gender = g
#         self.Age = a
    # def set_details(self): # self is a inbuilt keyword special for oops
    #     self.roll_no = int(input("Enter Your ROll No: "))
    #     self.name = input("Enter Your name: ")
    #     self.Gender = input("Enter Your Gender: ")
    #     self.Age = int(input("Enter Your Age: "))

#     def display_details(self):
#         print(f"ROll_No is: {self.roll_no}")
#         print(f"Name is: {self.name}")
#         print(f"Gender is: {self.Gender}")
#         print(f"Age is: {self.Age}")

# student1 = Students()
# student1.roll_no = 331
# student1.name = "Yuvraj Singh"
# student1.Gender = "Male"
# student1.Age = 21

# Output

# ROll_No is 331
# Name is Yuvraj Singh
# Gender is Male
# Age is 21

# ? but we can still see lot's of variable what if their is new student and we have to go throgth with same process one more time  : we can make another method that except the new student value for everynew student

# student1.set_details(331,"Yuvraj Singh" ,"Male", 21) # calling it and entering value
# student1.display_details()

# By just writing 3 line of code we can create a new student

# ? But can we make it even smaller: Yes, when we pass in the set_details their are already variable made that just get oevrride so we can just remove the variable, like below

# class students():
#     def set_details(self,roll_no:int, name:str, gender:str, age:int):
#         self.roll_no = roll_no
#         self.name = name
#         self.gender = gender
#         self.age = age

#     def display_details(self):
#         print(f"RollNo: {self.roll_no}")
#         print(f"Name: {self.name}")
#         print(f"Gender: {self.gender}")
#         print(f"Age: {self.age}")

# student1 = students()
# student1.set_details(331, "Yuvraj Singh", "Male", 21)
# student1.display_details() 

# ? We just remove the variable assingment that have been override with very new students details

# ! and their is another inbuilt method in which the method called itself automaticlly

# class students():
#     def __init__(self,roll_no:int, name:str, gender:str, age:int):
#         self.roll_no = roll_no
#         self.name = name
#         self.gender = gender
#         self.age = age

#     def display_details(self):
#         print(f"RollNo: {self.roll_no}")
#         print(f"Name: {self.name}")
#         print(f"Gender: {self.gender}")
#         print(f"Age: {self.age}")

# student1 = students(331,"Yuvraj Singh","Male", 21) # Hello: We don't even called the method it's automaticlly called
# # so we can just pass the set_details variable inside the init method
# student1.display_details()

# ? Example Question

# class student:
#     def __init__(self,name:str,age:int,marks:list[int]):
#         self.name = name
#         self.age =  age
#         self.marks = marks

#     def total(self)-> int:
#         return sum(self.marks)

#     def average(self)->float:
#         return sum(self.marks) / len(self.marks)

#     def grade(self)->None:
#         avg = self.average()
#         if avg >=90:
#             print("A")
#         elif avg >= 50 and avg <=89:
#             print("B")
#         else:
#             print("C")

# student1 = student("Yuvraj Singh", 21, [78, 54, 19,63])
# total = student1.total()
# print(total)
# avg = student1.average()
# print(avg)
# student1.grade()

# ? Class Variable And Instance Variable

# class Student:
#     school ="Holy Cross High School" # This is class variable. can be access by any object 

#     def __init__(self,name:str):
#         self.name = name # This is called instance variables 

# student1 = Student("Yuvraj Singh")
# student2 = Student("Ayush Singh")
# print(student1.name) # ? This are instance variable
# print(student2.name) # This are instance variable

# print(student1.school) # ? This is class variable: Holy Cross High School
# print(student2.school) # This is class variable: Holy Cross High School

# ? First way to change class variable

# Student.school = "XYZ"
# print(student1.school) # XYZ
# print(student2.school) # XYZ

# ? if i want to change only student1 or student2 school we can do by

# student1.school = "XYZ"
# print(student1.school) # XYZ