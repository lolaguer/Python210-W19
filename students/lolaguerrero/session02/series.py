## Fibonacci ##

def fibonacci(n):

    """ Return the nth value in the fibonacci series.
    Fibonnacci series: 0, 1, 1, 2, 3, 5, 8, 13, ...  """

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        ans = fibonacci(n-2) + fibonacci(n-1)
        return ans

# Testing Fibonacci series
print ('Testing Fibonacci:')
for i in range(0,10):
    print (fibonacci(i))



## Lucas ##

def lucas(n):

    """ Return the nth value in the lucas series.
      Lucas series is similar to fibonacci but it starts with the values 2 and 1:
      2, 1, 3, 4, 7, 11, 18, 29, ... """

    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        ans = lucas(n-2) + lucas(n-1)
        return ans

# Testing Lucas series
print ('Testing Lucas:')
for i in range(0,10):
    print (lucas(i))



## Generalizing ##

def sum_series(n, v1=0, v2=1):

    """ Calling this function with no optional parameters will produce numbers from the fibonacci series.
        Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers """

    if (v1 == 2) and (v2 == 1):
        if n == 0:
            return 2
        elif n == 1:
            return 1
        else:
            ans = sum_series(n - 2, v1=2, v2=1) + sum_series(n - 1,  v1=2, v2=1)
    else:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        else:
            ans = sum_series(n - 2) + sum_series(n - 1)

    return ans


# Asserting the general serie
print ('Testing sum_series:')
assert (fibonacci(9)  == sum_series(9))
assert (fibonacci(13) == sum_series(13))
assert (lucas(9) == sum_series(9, v1=2, v2=1))
assert (lucas(13) == sum_series(13, v1=2, v2=1))
print ('No problem with the general serie')