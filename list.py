# Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)

# Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]


mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)

# Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])


# Negative indexing means start from the end

# -1 refers to the last item, -2 refers to the second last item etc.

# Example
# Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


# Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#   Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# Insert at end

thislist = ["apple", "banana", "cherry"]

thislist.insert(len(thislist), "watermelon")
# or
thislist.append("ye")  # Better for end
print(thislist)


# Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop(
    1
)  # If you do not specify the index, the pop() method removes the last item.
print(thislist)


# The del keyword also removes the specified index:

# Example
# Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist


# The clear() method empties the list.

# The list still remains, but it has no content.

# Example
# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


"""LOOP THROUGH LISTS"""

# Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


#   Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])


# Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1


#   A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


# With list comprehension you can do all that with only one line of code:

# Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# Sort

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#  Case sensitive

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


# Copy list

# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Join Lists

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)