#!/usr/bin/python

# Create a wrapper function, perhaps safe_input()
# that returns None rather rather than raising these exceptions,
# when the user enters ^C for Keyboard Interrupt,
# or ^D (^Z on Windows) for End Of File.

def safe_input():
    try:
        return input('Hello, write something to print: ')
    except EOFError:
        print('EOFError')
        return None
    except KeyboardInterrupt:
        print ('KeyboardI')
        return None

print (safe_input())