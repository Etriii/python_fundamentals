"""
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.
"""

import re
#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")


import re
#Return a list containing every occurrence of "ai":
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


# Return an empty list if no match was found:
import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

# Search for the first white-space character in the string:
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start()) 

# Make a search that returns no match:
import re
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)#None

"""The split() function returns a list where the string has been split at each match:

Example
Split at each white-space character:
"""
import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


import re
#Split the string at the first white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)#['The', 'rain in Spain']


# The sub() function replaces the matches with the text of your choice:
# Example
# Replace every white-space character with the number 9:

import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)#The9rain9in9Spain


"""
You can control the number of replacements by specifying the count parameter:

Example
Replace the first 2 occurrences:
"""
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)#The9rain9in Spain


"""Match Object
A Match Object is an object containing information about the search and the result.

Note: If there is no match, the value None will be returned, instead of the Match Object."""


# Do a search that will return a Match Object:
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object


