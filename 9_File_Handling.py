
# ! What is file handling: So far, all the data in python programs disappers the movement the program ends. variable, lists, dictionary gone 

# but in real world we need data to be save to generate reports, export result, write log

# ? Their are some rules before learning about file handling

# When we dealing form file we have to always open it do the opereation read / Write and then close. close is mandarory

# ? open a file for reading
# f = open("text.txt","r")

# # ? Always close it when done
# f.close()

# ! file modes

# "r" : open for reading and file must exist. 
# "w" : create a new file or overwrite existing file
# "a": Add the content to the end of the file
# "x": create a file and if the file exist it throw the error
# "b": use with images pdf and video's 
# "t":treat data as text
# "+": used to combine modes

# ? read mode

# f = open("text.txt","r")
# content = f.read()
# print(content) # Output will be file content
# f.close() 

# ? But their is disadvantage by using read because it contain space in RAM and if file contain 100000 lines of code it will crash, frezzer or your pc or laptop can also get slow

# f = open("text.txt", "r")
# content = f.read(10) # this 10 is nothing just first 10 character will print
# print(content) # Hello Ayus

# ? Using with: When we are using with we don't need to close the file and it's very helpful. if we don't use with in code their is an error the file don't get close

# with open("text.txt","r") as f:
#     content = f.read()
#     print(content)

# ? readline and readlines

# with open("text.txt","r") as f:
#     content = f.readline() # readline reads a full line
#     print(content)

# ? readlines

# with open("text.txt","r") as f:
#     content = f.readlines() # it will read whole file and give it list
#     print(content)

# ? The most efficent way to loop throw a file is using for loop. suppose their is 10000 lines of code and you want to loop throw all. the memory usage will aslo will be low 

# with open("text.txt","r") as f:
#     content = f.readlines()
#     for i in range(len(content)):
#         print(content[i])

# ? write mode:

# with open("greeting.txt","w") as f:
#     content = f.write("Hello World! \n")
#     content = f.write("Ayush Singh\n")

# with open("greeting.txt","r") as f:
#     content = f.readlines()
#     print(content)

# TODO: write mode only take str not number or lists

# score = 95
# with open("greeting.txt","w") as f:
#     f.write(str(score)) 

# ? writelines: suppose we have list of string.

# lines = ["Hello my name is Ayush \n","I live in mumbai\n","Currently i'm learning python"]

# with open("greeting.txt","w") as f:
#     f.writelines(lines)

# ? append:

# with open("greeting.txt","a") as f:
#     f.write("\nAhhh") # it will add at the end of the file

# ? exclusive mode: "x": exclusive mode create a new file but if the file already exist it will throw an error


# ? absolute path and relative path

# Absolute path is nothing just the path of where your follwing folder is present and you give the path like c:user/window/..../filename

# relative path is like give the path where the folder is present within the folder in which you are working it mainly like "text.txt"

# ? The os.path module: This is the traditional way to work with path in python

# import os
# ? This is used to check for file and folder both
# print(os.path.exists("text.txt")) # True # This will return true or false

# ? if we want to check specifically for file 
# print(os.path.isfile("text.txt"))

# ? Specifically for folder
# print(os.path.isdir("part2"))

# ? Used to return file size
# print(os.path.getsize("text.txt")) # 629 in bytes

# os.path.join("data","logs","app.logs") # ? is used to join the path

# ! Modern way to work with files: using pathlib

# ? We have first import path
# from pathlib import Path # and same as traditional way we can check it

