#!/usr/bin/env python3

# ----------------------------------#
# Assignment: list_lab.py
# Author: Lola Guerrero
# RRoot, 01/29/2019, Created file
# ----------------------------------#


#########################
print ('## Series 1 ##')
#########################

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
# Display the list.
print(fruit_list)

# Ask the user for another fruit and add it to the end of the list.
new_fruit = input('Please tell me one fruit: ')
fruit_list.append(new_fruit)
# Display the list.
print(fruit_list)

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number.
fruit_number = int(input('Please tell a number between 1 and {}: '.format(len(fruit_list))))
print('You gave me the number {} and this number corresponds to this fruit {}'.format(fruit_number,fruit_list[fruit_number - 1]))

# Add another fruit to the beginning of the list using “+” and display the list.
new_fruit2 = input('Please tell me another fruit: ')
fruit_list = [new_fruit2] + fruit_list
print(fruit_list)

# Add another fruit to the beginning of the list using insert() and display the list.
new_fruit3 = input('Please tell me another fruit: ')
fruit_list.insert(0, new_fruit3)
print(fruit_list)

# Display all the fruits that begin with “P”, using a for loop.
fruits_start_P = []
for fruit in fruit_list:
    if fruit.lower().startswith('p'):
        fruits_start_P.append(fruit)
print('These are all the fruits that starts with "P/p": {}'.format(', '.join(fruits_start_P)))



#########################
print ('## Series 2 ##')
#########################

# Display the list.
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_list)

# Remove the last fruit from the list.
print ('Removing the last fruit from the list: ', fruit_list.pop())
# Display the list.
print(fruit_list, '\n')

# Ask the user for a fruit to delete, find it and delete it.
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_list, '\n')
del_fruit = input('Tell me which fruit would you like to remove: ')
if del_fruit not in fruit_list:
    del_fruit = input('Tell me which fruit would you like to remove: ')
else:
    fruit_list.pop(fruit_list.index(del_fruit))
print ('Here is the list without the fruit: {}'.format(fruit_list), '\n')


# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
x2fruit_list = fruit_list*2
flag = True
while flag:
    del_fruit = input('Tell me which fruit would you like to remove: ')
    print ('borrar', del_fruit)

    if del_fruit not in x2fruit_list:
        del_fruit = input('Tell me which fruit would you like to remove: ')
    else:
        [x2fruit_list.pop(i) for i, x in enumerate(x2fruit_list) if x == del_fruit]
        print(x2fruit_list)
        flag = False



#########################
print ('## Series 3 ##')
#########################

# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
# Display the list.
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_list)

flag = True
new_fruit_list = []

for fruit in fruit_list:

    like_fruit = input('Do you like ' + fruit.lower() + '? ')

    if like_fruit.lower() == 'no':
        continue

    elif like_fruit.lower() == 'yes':
        new_fruit_list.append(fruit)
    else:
        like_fruit = input('Please say yes or no! ')
        while flag:
            if like_fruit.lower() == 'no':
                flag = False
            elif like_fruit.lower() == 'yes':
                new_fruit_list.append(fruit)
                flag = False
            else:
                like_fruit = input('Please say yes or no! ')

print('Here are the fruits you like: ', ', '.join(new_fruit_list))



#########################
print ('## Series 4 ##')
#########################

# Make a new list with the contents of the original, but with all the letters in each item reversed.
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_list)

reversed_list = []

for fruit in fruit_list:
    reversed_fruit = fruit[::-1]
    reversed_list.append(reversed_fruit)

print (reversed_list, '\n')


# Delete the last item of the original list. Display the original list and the copy.
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print ('Original list', fruit_list)
fruit_list.pop()
print ('Copy list', fruit_list)


