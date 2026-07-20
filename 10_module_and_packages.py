
# ! What is module?: A module is simply a python file that contain code and that code can be reuse elsewhere

# why use module?: As project or program grows putting everything in one place become nightmare.

# module solve this by letting us to organic code into logical, spreated files 
# Reuse the same code across diffrent file
# Avoid duplicates- write ones import everywhere
# Collaborate - diffrent people work on diffrent module
# maintains is easy- fixing bug are easy

# ? How to use it

# import math  # Recommanded

# print(math.sqrt(16)) # 4
# print(math.floor(5.55)) # 5
# print(math.ceil(2.002)) # 3

# import random

# print(random.random()) # it will generate random number everytime we run it

# print(random.randint(1,6)) # it will return random number form given range

# print(random.choice([1,6])) # it will take a list and give any random value

# lst = [1,2,3,4,5]

# random.shuffle(lst) # it will take a list and generate a the list in random order
# print(lst)

# ? What is the datetime module?: 
# ? The datetime module is used for working with:

# Date
# Time
# Date + Time
# Time difference
# Time zones

# ? getting today's date
# from datetime import date

# today = date.today()
# print(today) # today's date

# ? current date and time

# from datetime import datetime

# now = datetime.now()
# print(now) # 2026-07-20 20:44:41.911633

# ? we can also create our own date

# from datetime import date

# d = date(2026,7,20)
# print(d)

# ? creating our own datetime

# from datetime import datetime

# dt = datetime(2026,7,26,14,54,28)
# print(dt) # 2026-07-26 14:54:28

# ? format date: we can format the date how i want

# from datetime import datetime

# now = datetime.now()
# print(now.strftime("%d/%m/%Y"))

"""
Common format codes:


| Code | Meaning        |
| ---- | -------------- |
| `%d` | Day            |
| `%m` | Month          |
| `%Y` | Year (2026)    |
| `%y` | Year (26)      |
| `%H` | Hour (24-hour) |
| `%I` | Hour (12-hour) |
| `%M` | Minute         |
| `%S` | Second         |
| `%A` | Weekday        |
| `%B` | Month name     |
"""

# print(now.strftime("%A"))

# ? Converting string into date

# from datetime import datetime

# s = "20-07-2026"
# d = datetime.strptime(s, "%d-%m-%Y")
# print(d)

# ? We can also find out diffrent between dates

# from datetime import date

# d1 = date(2026, 7, 20)
# d2 = date(2026, 8, 5)

# diff = d2 - d1

# print(diff) # 16 days, 0:00:00
# and if we want days only

# print(f"{diff.days} days") # 16 days


# ? Using timedelta: add or substract days

# from datetime import datetime, timedelta

# today = datetime.now()

# future = today + timedelta(days=10)

# print(f"{future.day} days") # 30

# today = datetime.now()

# past = today - timedelta(days= 5)
# print(f"5 days previous dates was {past.day} ")

# ? We can same do with hours and minutes

# after = today + timedelta(hours=5)

# after = today + timedelta(minutes=90)

# ? We can find you which day is today

# from datetime import datetime

# now = datetime.now()

# print(now.weekday()) # 0

"""
0 Monday
1 Tuesday
2 Wednesday
3 Thursday
4 Friday
5 Saturday
6 Sunday
"""

# ? Interview Question : Find Age

# from datetime import date

# birth =date(2004,7,26)
# today = date.today()

# age = today.year - birth.year

# if (today.month, today.day) < (birth.month, birth.day):
#     age -= 1

# print(age)

# ? What is packages: Packages are nothing just a bunch of file in one folder and that folder is called as package

# suppose i have 10 Files
"""
1
2
3
4
5
6
7
8
9
10
"""

# ? This all files are called module because it contain cretain type of code init
# ? but if we keep all this file in a folder is called as package and the folder should named as "__init__.py" and it should be empty

# shape -> Now this folder will be treated as package
#   __init__.py
#     1
#     2
#     3
#     4
#     5
#     6
#     7
#     8
#     9
#     10

# Let's create it: i have cretaed packages in python folder in which i have do this

# ? Absolute vs relative import : recommented is "Absolute pathing"

# from myapp.models.user import user # like this