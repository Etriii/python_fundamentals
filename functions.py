# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.


def my_function():
    print("Hello from a function")


my_function()


# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


# This function expects 2 arguments, and gets 2 arguments:
# By default, a function must be called with the correct number of arguments. Meaning that if your function
# expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")

"Arbitrary Keyword Arguments, *kwargs"
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:


# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")

"Arbitrary Keyword Arguments, **kwargs"
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

"Default Parameter Value"
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("India")
my_function()

"Return Vaulues"
# To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x

print(my_function(3))

"Positional-Only Arguments"
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:
def my_function(x, /):
  print(x)

my_function(3)#doesnt allow this my_function(x = 3)

"Keyword-Only Arguments"
# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, x):
  print(x)

my_function(x = 3)# doesnt allow this my_function(3)

"COMBINE Positional and Keyword Only Arguments"
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

"Recursion"
# Recursion is a common mathematical and programming concept. It means that a function 
# calls itself. This has the benefit of meaning that you can loop through data to reach 
# a result.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)