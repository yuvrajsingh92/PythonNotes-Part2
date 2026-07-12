# original = [1,2,3]
# copy = original
# copy.append(100)
# print(copy) # [1,2,3,100]
# print(original) # [1,2,3,100] # ? We have made the changes in the copy list but the original list also get affected

# ! why this happens? : When we assingn a variable that contain mutable object to a variable it does't give copy the value of the object but the hole id of the variable
# here is the below example

# original = [1,2,3]
# copy = original
# copy.append(100)
# print(copy,id(copy)) # [1,2,3,100] id = 2988475989120
# print(original,id(original)) # id = 2988475989120

# ! So how can we avoid it? : Their are two ways 1) shallow copy. 2) Deep Copy

# ? Shallow copy 

# abc = [1,2,3]
# ijk = abc.copy()
# print(abc,id(abc)) # 2400132847872
# print(ijk,id(ijk)) # 2400132845952
# ? we can cross check by appening element
# ijk.append("Ayush")
# print(abc) # [1, 2, 3,]
# print(ijk) # [1, 2, 3, 'Ayush']
# Their address are diffrent and this is how we can shallow copy 

# ! Deep copy

# abc = [1,2,3,[84,76,29,82],4,5,6]
# efg = abc.copy()

# efg[3][1] = 1000
# print(abc) #  [1, 2, 3, [84, 1000, 29, 82], 4, 5, 6]
# print(efg) # [1, 2, 3, [84, 1000, 29, 82], 4, 5, 6]

# ? it suppose to be make changes in efg but it make changes into abc also 
# and we try to add a element inside efg it will work

# efg.append("Ayush")
# print(efg) # [1, 2, 3, [84, 1000, 29, 82], 4, 5, 6, 'Ayush']
# but it did't make changes into abc. here deep coping comes in place

# ? The reason this happens is when we use shallow copy it will only work in other part not the inner part 

# ? if we use deepcopy we can overcome this problem. we have to first import copy

# import copy
# abc = [1,2,3,[84,76,29,82],4,5,6]
# efg = copy.deepcopy(abc)

# efg[3][1] = 1000
# print(abc) #  [1, 2, 3, [84, 76, 29, 82], 4, 5, 6]
# print(efg) # [1, 2, 3, [84, 1000, 29, 82], 4, 5, 6] 

# ! Passing by Refrence & value

# def add_num(x):
#     x = x + 1
#     print(f"inside function {x}") # 11
# x = 10
# add_num(x)
# print(f"Outside function {x}") # 10 

# ? This is called by value

# ? Now pass by refrence

# def add_list(num:list):
#     num.add(100)
#     print(num) # [1,2,3,100] # The original list got changed
# num = [1,2,3]
# print(add_list(num))
# print(num) # [1,2,3,100] # We did't add to the outer list then why this got added? : when we pass a mutable object this happens. if we try to add immutable object this won't happens

# ? To overcome this we use deepcopy

# import copy
# def add_num(num:list):
#     num = copy.deepcopy(num)
#     num.append(100)
#     print(f"inner list {num}") # [1,2,3,100]
# num = [1,2,3]
# add_num(num)
# print(f"Outer Copy {num}") # [1,2,3]

# ! Type annotations

# def calculate(a,b):
#     return a + b
# print(calculate("Ayush","Singh")) # In this case we can pass any data, but what if we want only boolean or int 

# ? so the best practices is give the type of parameter of what data is going to come

# def calculate(a:int,b:int) -> int: # Like giving it what value is going to come
#     return a + b
# print(calculate(1,2))

# ? Advance Annotations: When we know that this particular object only contain specific type of value

# def max_num(marks:list[int]):
#     return max(marks)
# marks = [1,2,3,4,5,"Ayush"]
# print(max_num(marks)) # But what if in the list i pass string. it will throw error

# ? What if in that single object their can be string and int both are their 

# def addlist(lst:list[int | str]): # by using pipe we can multiple type of datatype
#     lst.append("Ayush")
#     return lst
# data = [1,2,3,4,5]
# print(addlist(data)) 