def FizzBuzz():

    """ From 1 to 100 inclusive, return "Fizz" for multiples of three,
       “Buzz” for the multiples of five,
       and "FizzBuzz" for multiples of both three and five """

    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print('FizzBuzz')
        elif i % 3 == 0:
            print ('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print (i)

print (FizzBuzz())








