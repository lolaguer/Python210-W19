# Part 2:

def print_grid(n):
    m = int(n / 2)
    for i in range (0, 2):
        print ('+' + ('-' * m) + '+' + ('-' * m) + '+')
        for i in range(0, m):
            print ('|' + (' ' * m) + '|' + (' ' * m) + '|')
    print ('+' + ('-' * m) + '+' + ('-' * m) + '+')


print (print_grid(3))
print (print_grid(9))



# Part 3:

def print_grid2(number, size):

    for i in range (0, number):
        print (('+' + ('-' * size)) * number + '+')
        for i in range(0, size):
            print (('|' + (' ' * size)) * number + '|')
    print(('+' + ('-' * size)) * number + '+')


print_grid2(5,3) ## 5 number of squares, 3 size squares
print_grid2(3,5) ## 3 number of squares, 5 size squares