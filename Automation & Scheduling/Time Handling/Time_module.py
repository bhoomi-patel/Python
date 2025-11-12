'''The time module is best for simple, OS-level time operations,
 like measuring performance or pausing execution. It mostly deals with "Epoch time".
 Epoch time (Unix Timestamp) - Returns the current time as a floating-point number  --> The number of seconds that have elapsed since January 1st, 1970, 00:00:00 UTC. 
'''
import time

# get the current time as a Unix timestamp
current_timestamp = time.time()
print(f"Current timestemp: {current_timestamp}")

# 2 - sleep - pause execution
import time
print("Task started.")
time.sleep(2) # pause for 2 second 
print("Task resumed after 2 sec.")

# Example - Write a script that prints the numbers 1 to 5, with a 1-second delay between each number.
import time 
for i in range(1,6):
    print(i)
    time.sleep(1)
print("Task completed")

# TASK - Create a function to measure how long a piece of code takes to execute.
import time
def measure_time(fun):
    '''decorator that prints how long function takes to execute.'''
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = fun(*args,**kwargs)
        end_time=time.time()
        print(f"{fun.__name__} took {end_time - start_time:.6f} seconds to run.")
        return result
    return wrapper
@measure_time
def complex_calculation():
    '''Afunction that takes some time to run'''
    time.sleep(2) 
    return 42 
result = complex_calculation()

# 3 - Timestamp to String : time.ctime(seconds)
# Converts a timestamp to a human-readable string.
import time 
# Current time as a string
current_time_string = time.ctime()
print (f"Current time : {current_time_string}")
#  Convert a specific timestamp to a string
moon_landing = 0 # Epoch start
print(f"Epoch start : {time.ctime(moon_landing)}")