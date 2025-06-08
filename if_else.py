a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


# One line if statement:

if a > b:
    print("a is greater than b")

# One line if else statement:
a = 2
b = 330
print("A") if a > b else print("B")#B

# i think this is also called a ternary operator


# nested if

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")