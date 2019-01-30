#!/usr/bin/env python3

# ----------------------------------#
# Assignment: strformat_lab.pypy
# Author: Lola Guerrero
# RRoot, 01/29/2019, Created file
# ----------------------------------#


########################
print ('## Task One ##')
########################

item = (2, 123.4567, 10000, 12345.67)
print ('file_00 %s:'  % item[0], '%.2f' % item[1], '%.2e' % item[2], '%.2e' % item[3])



########################
print ('## Task Two ##')
########################

item = (2, 123.4567, 10000, 12345.67)
item0, item1, item2, item3 = item
print ('file_00{0}: {1:.2f}, {2:.2e}, {3:.2e}'.format(item0, item1, item2, item3))



##########################
print ('## Task Three ##')
##########################

def formatter(in_tuple):

    len_tuple = len(in_tuple)
    form_string = '{:d} ' * (len_tuple)
    form_string = form_string.strip()
    form_string = form_string.replace(' ', ', ')
    return 'the {} numbers are {}'.format(len_tuple, form_string.format(*in_tuple))

print (formatter((2,3,5)))
print (formatter((2,3,5,7,9)))


#########################
print ('## Task Four ##')
#########################

item = (4, 30, 2017, 2, 27)
item0, item1, item2, item3, item4 = item
print ('{0:0>2d}, {1:0>2d}, {2:0>2d}, {3:0>2d}, {4:0>2d}'.format(item3, item4, item2, item0, item1))



#########################
print ('## Task Five ##')
#########################

item  = ['oranges', 1.3, 'lemons', 1.1]

print (f"The weight of an {item[0][:-1]} is {item[1]} and the weight of a {item[2][:-1]} is {item[3]}")
print (f"The weight of an {item[0][:-1].upper()} is {item[1]*1.2} and the weight of a {item[2][:-1].upper()} is {item[3]*1.2}")



########################
print ('## Task Six ##')
########################

header = "Name, Age, Cost"
p1 = 1, "Bob Smith", "23", "100"
p2 = 2, "Sue Jones", "45", "100000"

table = p1, p2

form_string = '{:20}, {:.0f}, {:8}'

for row in table:
    print (form_string.format(*row))  # Need to finish it