#!/usr/bin/env python3

# ----------------------------------#
# Assignment: dic_lab.py
# Author: Lola Guerrero
# RRoot, 02/01/2019, Created file
# ----------------------------------#


##############################
print ('## Dictionaries 1 ##')
##############################

# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”
dict1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

# Display the dictionary
print (dict1)

# Delete the entry for “cake”
dict1.pop("cake")

# Display the dictionary
print (dict1)

# Add an entry for “fruit” with “Mango” and display the dictionary
dict1["fruit"] = "Mango"

# Display the dictionary keys
print (dict1.keys())

# Display the dictionary values
print (dict1.values())

# Display whether or not “cake” is a key in the dictionary
print ("cake" in dict1)

# Display whether or not “Mango” is a value in the dictionary
print ("Mango" in dict1.values())


##############################
print ('## Dictionaries 2 ##')
##############################

# Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s
# in each value as the value (consider upper and lower case?).

def count_t(letter):
    count = 0
    for l in letter:
        if l == 't':
            count +=1
    return count

dict2 = dict((k, count_t(v)) for k, v in dict1.items())
print (dict2)


######################
print ('## Sets 1 ##')
######################

# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4
s2 = set()
for i in range(0,20):
    if i % 2 == 0:
        s2.add(i)

s3 = set()
for i in range(0,20):
    if i % 3 == 0:
        s3.add(i)

s4 = set()
for i in range(0,20):
    if i % 4 == 0:
        s4.add(i)

# Display the sets
print (s2)
print (s3)
print (s4)

# Display if s3 is a subset of s2 (False)
print (s3 < s2)

# and if s4 is a subset of s2 (True)
print (s4 < s2)



######################
print ('## Sets 2 ##')
######################

# Create a set with the letters in ‘Python’ and add ‘i’ to the set
s_python = {"P", "y", "t", "h", "o", "n"}
s_python.add("i")
print (s_python)

# Create a frozenset with the letters in ‘marathon’
f_set = frozenset(("m", "a", "r", "a", "t", "h", "o", "n"))
print (f_set)

# Display the union and intersection of the two sets
# Union
print (s_python | f_set)
# Intersection
print (s_python & f_set)