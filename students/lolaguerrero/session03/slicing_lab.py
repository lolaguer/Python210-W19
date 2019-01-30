#!/usr/bin/env python3

# ----------------------------------#
# Assignment: slicing_lab.py
# Author: Lola Guerrero
# RRoot, 01/29/2019, Created file
# ----------------------------------#


# First_last
def exchange_first_last(seq):

    """ Return the original sequence with first and last items exchanged."""

    if isinstance(seq, tuple):
        return (seq[-1],) + seq[1:-1] + (seq[0], )
    elif isinstance(seq, list):
        return [seq[-1]] + seq[1:-1] + [seq[0]]
    else:
        return seq[-1]+ seq[1:-1] + seq[0]


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [2, 54, 13, 12, 5, 32]

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert exchange_first_last(a_list) == [32, 54, 13, 12, 5, 2]



# remove_every_other
def remove_every_other(seq):

    """ Return the original sequence with every other item removed."""

    return seq[::2]


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [2, 54, 13, 12, 5, 32]

assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) == (2, 13, 5)
assert remove_every_other(a_list) == [2, 13, 5]




# remove_4first_4last
def remove_4first_4last(seq):

    """ Return the original sequence with every other item removed."""
    new_seq = seq[4:-4]
    return new_seq[::2]


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32, 44, 56, 60)
a_list = [2, 54, 13, 12, 5, 32, 44, 56, 60]

assert remove_4first_4last(a_string) == " sas"
assert remove_4first_4last(a_tuple) == (5,)
assert remove_4first_4last(a_list) == [5]


# reverse_sequence
def reverse_sequence(seq):

    """ Return the original sequence with the elements reversed """
    return seq[::-1]


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32, 44, 56, 60)
a_list = [2, 54, 13, 12, 5, 32, 44, 56, 60]

assert reverse_sequence(a_string) == "gnirts a si siht"
assert reverse_sequence(a_tuple) == (60, 56, 44, 32, 5, 12, 13, 54, 2)
assert reverse_sequence(a_list) == [60, 56, 44, 32, 5, 12, 13, 54, 2]



# last_first_middle_third
def last_first_middle_third(seg):
    """ Return the last third, then first third, then the middle third in the new order"""
    # To-Do
