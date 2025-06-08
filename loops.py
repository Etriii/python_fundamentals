# With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
    print(i)
    i += 1

# With the break statement we can stop the loop even if the while condition is true:
# Example
# Exit the loop when i is 3:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# With the continue statement we can stop the current iteration, and continue with the next:
# Example
# Continue to the next iteration if i is 3:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# With the else statement we can run a block of code once when the condition no longer is true:
# Example
# Print a message once the condition is false:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


# Print each fruit in a fruit list: (foreach)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Loop through the letters in the word "banana":
for x in "banana":
    print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
# Example
# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
    print(x)

"NESTED LOOPS"
# 1D Loop (Single loop)
for i in range(3):
    print(i)
    
# 0
# 1
# 2

# 2D
for i in range(2):  # Outer loop
    for j in range(3):  # Inner loop
        print(f"i={i}, j={j}")
        
# OUTPUT 
# i=0, j=0
# i=0, j=1
# i=0, j=2
# i=1, j=0
# i=1, j=1
# i=1, j=2

# 3D
for i in range(2):
    for j in range(2):
        for k in range(2):
            print(f"i={i}, j={j}, k={k}")

# OUTPUT 
# i=0, j=0, k=0
# i=0, j=0, k=1
# i=0, j=1, k=0
# i=0, j=1, k=1
# i=1, j=0, k=0
# i=1, j=0, k=1
# i=1, j=1, k=0
# i=1, j=1, k=1

for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                print(f"i={i}, j={j}, k={k}, l={l}")

# OUTPUT
# i=0, j=0, k=0, l=0
# i=0, j=0, k=0, l=1
# i=0, j=0, k=1, l=0
# i=0, j=0, k=1, l=1
# i=0, j=1, k=0, l=0
# ...
# i=1, j=1, k=1, l=1