# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


"""
NUMBERS
"""

x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# Casting

x = int(1)  # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3

x = float(1)  # x will be 1.0
y = float(2.8)  # y will be 2.8
z = float("3")  # z will be 3.0
w = float("4.2")  # w will be 4.2

x = str("s1")  # x will be 's1'
y = str(2)  # y will be '2'
z = str(3.0)  # z will be '3.0'

# Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
    print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


#   Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)


# Slicing Strings (starts also at index 0)

b = "Hello, World!"
print(b[2:5])
# Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])


# Go up to but NOT including end
b = "Hello, World!"
print(b[-5:-2])  # output orl


"""MODIFY STRINGS"""
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"


# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))  # Jello, World!

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

"""Concantenate Strings"""
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

a = "Hello"
b = "World"
print(a, b)


"""Format String"""
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)





"""BOOLEAN"""

# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

# The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# In fact, there are not many values that evaluate to False, except empty values, such as 
# (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
# The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


