## Fibonacci ##

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        ans = fibonacci(n-2) + fibonacci(n-1)
        return ans


for i in range(0,10):
    print (fibonacci(i))



## Lucas ##

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        ans = lucas(n-2) + lucas(n-1)
        return ans


for i in range(0,10):
    print (lucas(i))



## Generalizing ##

def sum_series(n, v1=0, v2=1):

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


## Tests

assert (fibonacci(9)  == sum_series(9))
assert (fibonacci(13) == sum_series(13))
assert (lucas(9) == sum_series(9, v1=2, v2=1))
assert (lucas(13) == sum_series(13, v1=2, v2=1))