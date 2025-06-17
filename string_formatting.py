"""
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

Before Python 3.6 we had to use the format() method.

F-Strings
F-string allows you to format selected parts of a string.

To specify a string as an f-string, simply put an f in front of the string literal
"""



"""
Placeholders and Modifiers
To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.
"""

# Example
# Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)

"""
A placeholder can also include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
"""
# Example
# Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)#The price is 59.00 dollars


# You can also format a value directly without keeping it in a variable:

# Example
# Display the value 95 with 2 decimals:

txt = f"The price is {95:.2f} dollars"
print(txt)


"""
Perform Operations in F-Strings
You can perform Python operations inside the placeholders.

You can do math operations:
"""

# Example
# Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)


# Return "Expensive" if the price is over 50, otherwise return "Cheap":
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)#It is very Cheap


"""
Execute Functions in F-Strings
You can execute functions inside the placeholder:
"""

# Example
# Use the string method upper()to convert a value into upper case letters:

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)


# The function does not have to be a built-in Python method, you can create your own functions and use them:

# Example
# Create a function that converts feet into meters:
def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)


"Use a comma as a thousand separator:"
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)#The price is 59,000 dollars

# If you want to use more values, just add more values to the format() method:

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))#I want 3 pieces of item number 567 for 49.00 dollars.


# if you want to refer to the same value more than once, use the index number:
# Example
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))#His name is John. John is 36 years old.

"""Named Indexes"""
# You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
# Example
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

