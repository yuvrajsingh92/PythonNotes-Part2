
# ! What is multithreading: Multithreadling is process in which the program run without waiting for the code to run : Example if the code is taking sometime it will skip that part and run the next line of code by assinging the task to thread

# import threading
# import time

# def task():
#     print("Programming has started Running")
#     time.sleep(2)
#     print("Program has ended")
# task() # Programming has started Running \n Program has ended

# This was the output the first line have runned and for second line the program was holded for 2 sec

# ? Example of threading 

# def task():
#     print("Program is running") # 2
#     time.sleep(2)
#     print("Program Ended") # 4

# print("Main Program have started") # 1
# t = threading.Thread(target=task)
# t.start()
# print("Main Program have Ended") # 3

# This was the sequence in which the program have worked

# ? But what if the function have argument then how we can pass it?

# import threading 
# import time

# def task(name:str):
#     print(f"{name} is Running") # 2
#     time.sleep(2)
#     print(f"{name} is finished") # 4

# print("This is the main Program") # 1
# t1 = threading.Thread(target=task,args=("Cooking",))
# t2 = threading.Thread(target=task,args=("Baking",))
# t1.start()
# t2.start()
# print("Main Program ended") # 3

# ? In th above case the the main program is ended statement have run before the program have even ended and that's not right so how to overcome this

# import threading
# import time

# def task(name:str):
#     print(f"{name} is Started")
#     time.sleep(2)
#     print(f"{name} is finished")

# print("The Main Program have Started")
# t1 = threading.Thread(target=task,args=("Cooking",))
# t2 = threading.Thread(target=task,args=("Baking",))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("The Main Program have Ended")

"""

The Main Program have Started
Cooking is Started
Baking is Started
Cooking is finished
Baking is finished
The Main Program have Ended

""" # This is the Output of the Above code as it should be 

# ? But if we think about a second about the above code why it's is not taking 4 sec to run why it's only taking 2 sec to run for 2 times? because we have made threads 

# ! Their a think called as race condition

# import time
# import threading

# balance = 1000

# def withdraw(amount):
#     global balance
#     temp = balance
#     time.sleep(0.0001)
#     balance = temp - amount 

# t1 = threading.Thread(target=withdraw,args=(100,))
# t2 = threading.Thread(target=withdraw,args=(100,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(f"Before withdrawal the balance was 1000 and after 2 withdrawal of 100 the output should be 800 but the output is {balance} ") # 900

# ? This is happened because both the threads have been got the balance as 1000 and after withdrawal the of 100 900 remains and this is called as race condition

# ? To overcome this their is a method know as lock

# import time
# import threading

# balance = 1000
# lock  = threading.Lock()

# def withdraw(amount):
#     global balance
#     with lock:
#         temp = balance
#         time.sleep(0.0001)
#         balance = temp - amount 

# t1 = threading.Thread(target=withdraw,args=(100,))
# t2 = threading.Thread(target=withdraw,args=(100,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(f"Before withdrawal the balance was 1000 and after 2 withdrawal of 100 the output should be 800 and the output is {balance} ") # 800

# ? But we can see here is a problem that the number of threads we are creating we have to write the number of start, join. to overcome this their is a modern way

# from concurrent.futures import ThreadPoolExecutor
# import threading
# import time

# balance = 1000
# lock = threading.Lock()
# def withdraw(amount):
#     global balance
#     with lock:
#         temp = balance
#         time.sleep(0.0001)
#         balance = temp - amount
#         return balance

# withdraw_amount = [100,100,100]

# with ThreadPoolExecutor(max_workers= 3) as executors:
#     results = executors.map(withdraw,withdraw_amount)

# for result in results:
#     print(result)

# print(f"The final balance is {balance}") # Much more clean and simple


# ! Multiprocessing: 

# from multiprocessing import Process

# def task(name:str):
#     print(f"{name} running")

# if __name__ == "__main__": # We have to compalsory have to write this is otherwise multiple process can spawn
#     p1 = Process(target=task,args=("Process-1",))
#     p2 = Process(target=task,args=("Process-2",))
#     p1.start()
#     p2.start()
#     p1.join()
#     p1.join()


# ! When to use multithreading and muliprocessing?

# When we have to download file, API calls - Threading
# When we have to read/write many files - Threading
# When we have to use database queries - Threading

# When we have to do heavy maths operations - Multiprocessing
# When we have to do image/video processing - Multiprcessing

