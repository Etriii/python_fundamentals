"""Python allows for user input.

That means we are able to ask the user for input.

The following example asks for your name, and when you enter a name, it gets printed on the screen:"""


# Example
# Ask for user input:

print("Enter your name:")
name = input()
print(f"Hello {name}")
"""
Enter your name:
alex

Hello alex
"""



"Using prompt"
#In the example above, the user had to input their name on a new line. The Python input() function has a prompt
#parameter, which acts as a message you can put in front of the user input, on the same line:

# Add a message in front of the user input:
name = input("Enter your name:")
print(f"Hello {name}")


"Multiple Inputs"
# You can add as many inputs as you want, Python will stop executing at each of them, waiting for user input:


# Multiple inputs:
name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")


"""
Input Number
The input from the user is treated as a string. Even if, in the example above, you can input a number, the Python interpreter will still treat it as a string.

You can convert the input into a number with the float() function:
"""

# To find the square root, the input has to be converted into a number:
x = input("Enter a number:")

#find the square root of the number:
import math
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")



y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")

"""
Enter a number:
a

Wrong input, please try again.
Enter a number:
a

Wrong input, please try again.
Enter a number:
n

Wrong input, please try again.
Enter a number:
1

Thank you!
"""