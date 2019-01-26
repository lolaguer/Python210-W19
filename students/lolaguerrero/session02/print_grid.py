# # Part 2:

def print_grid(n):

    """ Write a function that draws a grid like the following:

            + - + - +
            |   |   |
            + - + - +
            |   |   |
            + - + - +

        Where the input will be the size of the grid """

    m = int(n / 2)
    for i in range (0, 2):
        print ('+' + ('-' * m) + '+' + ('-' * m) + '+')
        for i in range(0, m):
            print ('|' + (' ' * m) + '|' + (' ' * m) + '|')
    print ('+' + ('-' * m) + '+' + ('-' * m) + '+')



while True:

    size = input('Choose a size for the grid or Exit to stop: ')

    if size.lower() == 'exit':
        break
    elif size == '':
        size = input('Choose a size for the grid or Exit to stop: ')
    else:
        print (print_grid(int(size)))






# Part 3:

def print_grid2(number, size):

    """ Write a function that draws a grid like the following:

                + - + - + - +
                |   |   |   |
                + - + - + - +
                |   |   |   |
                + - + - + - +
                |   |   |   |
                + - + - + - +


        Where the first input will be the number of grids and the second the size for each grid """

    for i in range (0, number):
        print (('+' + ('-' * size)) * number + '+')
        for i in range(0, size):
            print (('|' + (' ' * size)) * number + '|')
    print(('+' + ('-' * size)) * number + '+')



while True:

    number_size = input('Choose number of grids and its size or Exit to stop: ')
    number_size = ' '.join(number_size.split())

    if number_size.lower() == 'exit':
        break
    elif number_size == '':
        number_size = input('Choose number of grids and its size or Exit to stop: ')
    else:
        if ',' in number_size:
            number_size = number_size.strip().replace(',', ' ')

        print ('size number', number_size)

        number_size = ' '.join(number_size.split())
        number, size = number_size.split(' ')
        print (print_grid2(int(number), int(size)))