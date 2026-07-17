
# ! What is Exception handiling: Expection handiling is the process in which their is an error occur on line number 11 and because of that next line code did't work. So to tackel this we use try and expect block and error names. And if we don't handle error it will cost us with program crash, user sees a ugly error, Bad User experience, sometime lose of data

# age = int(input("Enter your age: "))

# if age > 18:
#     print("Adult")

# else:
#     print("Babu ho tum")

# This code is very vurnalable. if i enter abc the code will throw error


# try:
#     age = int(input("Enter your Age: "))
#     if age >= 18:
#         print("Adult")
#     else:
#         print("Not Adult")

# except:
#     print("Some error occured") # because of this the below line of code is working

# print("Good")
# print("Accha")

# ? ZeroDivisionError: When we divide a number by 0 it will throw error

# print(3/3) # 1.1
# print(10/0) # ZeroDivisionError

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))

# print(f"num1 / num2 is {num1 / num2}")

# ? This are the example of ZeroDivisionError. we can overcome like above code but if we put abc then also some error is their and if divide by 0 then also it will give the same message how to know that this is the exact error

# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter a number: "))
#     print(f"num1 / num2 is {num1 / num2}")
# except ZeroDivisionError:
#     print("Can't divide by 0")
# except ValueError:
#     print("Please Enter a number Only")

# Their are common built in Exception

# ?ValueError: If we want age but the user enters "abc" or and other value except number. ValueError comes
# num = int(input("Enter Your Age: ")) 

# ? TypeError:# ? When we try to do operation on wrong type. eg: ("x" + 5)
# print("x"+5)
# ? ZeroDivisionError : When we try to divide any number by 0

# print(10/0)

# ? IndexError: When the list index get out of the range
# nums = [1,2,3,4,5]
# nums[5]

# ? KeyError: When we try to find 
# user = {"name": "Alice", "age": 25}
# print(user.get("email"))  

# ? AttributeError: Calling a missing method or attribute

# ? NameError : When variable does't exist

# FileNotFoundError: When file is not present at the given location

# KeyboardInterrupt:

# ? Capturing the Expection object

# ? In this case we don't know the error just a simple message
# try:
#     age = int(input("Enter your Age: "))
#     if age >= 18:
#         print("Adult")
#     else:
#         print("Not Adult")

# except:
#     print("Some error occured")

# ? Here we use Exception and print it and the name of error

# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter a number: "))
#     print(f"num1 / num2 is {num1 / num2} ")
# except Exception as e:
#     print(f"Error message is {e}")
#     print(f"Error type {type(e).__name__}")


# ? In this case we have use the else also after except. When try works perfectly else also work

# try:
#     num1 = int(input("Enter a value: "))
#     if num1 >= 18:
#         print(f"You can vote and get a driving licence")
#     else:
#         print(f"Age is less then 18")
# except Exception as e:
#     print(f"Error message {e} and erro is {type(e).__name__}")
# else:
#     print("Thank you!")

# ? We have another clause called as "finally": finally always get run

# try:
#     name = input("Enter Your name: ")
#     age = int(input("Enter your age :"))
# except Exception as e:
#     print(f"Error message is {e} and the error is \n {type(e).__name__}")

# finally:
#     print(f"Your name is {name} and your age is {age}")

# ? raising an error: raising an error is the process in which we raise keyword to get catch the error


# def check_age(age:int):
#     if age < 0:
#         raise ValueError("Age can't be negative ")
#     elif age >= 150:
#         raise ValueError("Age is not real ")
#     elif age == 00 or 0000 or 000:
#         print("Masti chal rahe hai idhar ?")
#     else:
#         print("Good age")


# try :
#     check_age(00000000)
# except Exception as e:
#     print(e)
# except Exception as e:
#     print(e)

# ? Custom exceptions: Creating Own error name 

# amount = 1000
# withdraw_amount = 5000

# if withdraw_amount > amount:
#     raise ValueError ("Insufficent balance") # ? Everywhere we put valueError that does't tell us the real issue so we use custom exceptions

# ? Example: we have to create a class first

# class InsufficientFundsError(Exception):
#     pass

# def withdram_money(balance, withdram_amount):
#     if balance < withdram_amount:
#         raise InsufficientFundsError("Insufficient balance")
#     print(f"Remaining Balance is {balance - withdram_amount}")
# try:
#     withdram_money(1000,200)
# except InsufficientFundsError as e:
#     print(f"Error is {e}")
# except Exception as e:
#     print(f"Error is {e}")
