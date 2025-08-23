# PYTHON FULL FUNDAMENTALS REFERENCE SCRIPT (WITH EXAMPLES AND COMMENTS)

# --------------------------
# VARIABLES AND DATA TYPES
# --------------------------
a = 10
b = 20.5
c = "Hello"
d = True
e = None
print(a, b, c, d, e)
print(type(a), type(b), type(c), type(d), type(e))

# Type casting
x = int(2.9)  # 2
y = float("3.14") # 3.14
z = str(100) # "100"
print(x, y, z)

# --------------------------
# OPERATORS
# --------------------------
# Arithmetic: + - * / % // **
# Comparison: == != > < >= <=
# Logical: and, or, not
# Assignment: = += -= *= ...
# Identity: is, is not
# Membership: in, not in

# --------------------------
# STRINGS
# --------------------------
name = "Python"
print(name[0])            # Indexing
print(name[-1])           # Negative Index
print(name[0:3])          # Slicing
print(name.upper())
print(name.lower())
print(name.replace("Py", "My"))
print("th" in name)
print(len(name))

# --------------------------
# CONDITIONALS
# --------------------------
age = 18
if age >= 18:
    print("Adult")
elif age > 13:
    print("Teen")
else:
    print("Child")

# --------------------------
# LOOPS
# --------------------------
for i in range(3):
    print(i)

j = 0
while j < 3:
    print(j)
    j += 1

# break, continue, pass
for i in range(5):
    if i == 3:
        break
    if i == 1:
        continue
    print(i)

# --------------------------
# FUNCTIONS
# --------------------------
def greet(name="Guest"):
    print("Hello", name)

greet("Alice")
greet()

def add(a, b):
    return a + b

print(add(10, 20))

# --------------------------
# LISTS
# --------------------------
lst = [1, 2, 3]
lst.append(4)
lst.insert(1, 5)
lst.remove(2)
lst.pop()
print(lst)
print(lst.index(5))
print(lst.count(1))
print(sorted(lst))
lst.clear()
print(lst)

# List comprehension
squares = [x*x for x in range(5)]
print(squares)

# --------------------------
# TUPLES
# --------------------------
tpl = (1, 2, 3)
print(tpl[1])

# --------------------------
# SETS
# --------------------------
s = {1, 2, 3, 2}
s.add(4)
s.remove(1)
s.discard(5)  # no error if element not found
print(s)
print(len(s))

# --------------------------
# DICTIONARIES
# --------------------------
d = {"name": "John", "age": 25}
print(d["name"])
d["city"] = "NY"
d.pop("age")
d.update({"email": "john@example.com"})
d.popitem()  # removes last inserted item
d.setdefault("gender", "Male")
print(d)
print(d.get("name"))
print("name" in d)
d.clear()
print(d)

# --------------------------
# FILE HANDLING
# --------------------------
# Writing
with open("sample.txt", "w") as f:
    f.write("Hello World\n")

# Reading
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# --------------------------
# EXCEPTION HANDLING
# --------------------------
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Execution finished")

# --------------------------
# OBJECT-ORIENTED PROGRAMMING
# --------------------------
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hello, my name is", self.name)

p = Person("Alice")
p.say_hi()

# Inheritance
class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def get_grade(self):
        return self.grade

s = Student("Bob", "A")
s.say_hi()
print(s.get_grade())

# Polymorphism
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Woof")

def make_sound(animal):
    animal.sound()

make_sound(Cat())
make_sound(Dog())

# --------------------------
# ENCAPSULATION
# --------------------------
class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account()
acc.deposit(1000)
print(acc.get_balance())

# --------------------------
# ABSTRACTION
# --------------------------
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print(c.area())

# --------------------------
# LAMBDA, MAP, FILTER, REDUCE
# --------------------------
from functools import reduce
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
evens = list(filter(lambda x: x%2==0, nums))
sum_all = reduce(lambda x,y: x+y, nums)
print(squares, evens, sum_all)

# --------------------------
# MODULES & PACKAGES
# --------------------------
import math
print(math.sqrt(16))

# --------------------------
# DATE AND TIME
# --------------------------
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# --------------------------
# REGULAR EXPRESSIONS
# --------------------------
import re
pattern = r"\d+"
text = "My number is 12345"
match = re.findall(pattern, text)
print(match)

# --------------------------
# JSON HANDLING
# --------------------------
import json
data = {"name": "John", "age": 30}
json_str = json.dumps(data)
print(json_str)
parsed = json.loads(json_str)
print(parsed)

# --------------------------
# GENERATOR
# --------------------------
def gen():
    for i in range(3):
        yield i

for val in gen():
    print(val)

# --------------------------
# DECORATORS
# --------------------------
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def say_hello():
    print("Hello")

say_hello()


