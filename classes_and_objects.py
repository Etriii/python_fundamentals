""" 
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.
"""

# To create a class, use the keyword class:
# Create a class named MyClass, with a property named x:
class MyClass:
  x = 5

# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)

"The __init__() Function"
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# constructor in other language
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

"The __str__() Function"
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:

# The string representation of an object WITHOUT the __str__() function:
# - <__main__.Person object at 0x15039e602100>
# if have
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)#John(36)

# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

"modify object properties"
p1.age = 40
"Delete Object Properties"
del p1.age
"Delete Objects"
del p1

"if you want to create functions or classes that you dont know the code body yet"
class Person:
    pass
def my_function():
    pass

for i in range(5):
    pass  # not doing anything yet

if 3<2:
    pass  # placeholder for logic

