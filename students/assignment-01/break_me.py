#-------------------------------------#

# Title: Task 1 - Explore Errors

# Lola Guerrero - Python210 Winter

# RRoot, 18/01/2019, Created File

#-------------------------------------#


# Each function, when called, should cause an exception to happen
# Each function should result in one of the four most common exceptions you’ll find.
# for review: NameError, TypeError, SyntaxError, AttributeError



def Excep_NameError():
    try:
        print (a)
    except NameError:
        print ('The variable a is not defined')

print (Excep_NameError())




def Excep_TypeError(x):
    try:
        print (32/x)
    except TypeError:
        print (x + ' has inappropriate type')

print (Excep_TypeError('4'))
print(Excep_TypeError(4))


def Excep_SyntaxError():
    try:
        print (3 /% 4)
    except SyntaxError:
        print('Review your expression')


print (Excep_SyntaxError())  #How do you make an exception in a SyntaxError??



def Excep_AttributeError():
    try:
        import string
        print (string.digit)
    except AttributeError:
        print('Attribute error')


print (Excep_AttributeError())


