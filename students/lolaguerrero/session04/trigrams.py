#!/usr/bin/env python3

# ----------------------------------#
# Assignment: trigrams.py
# Author: Lola Guerrero
# RRoot, 02/03/2019, Created file
# ----------------------------------#

import sys
import random
import string




def read_in_data(file):
    r_file = open(file, 'r')
    text = []
    for line in r_file:
        line = line.replace('\n', '')
        text.append(line)
    return ' '.join(text)



def make_words(text):
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    return text.translate(translator).split()



def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words) - 2):
        pair = words[i:i + 2]
        follower = words[i + 2]
        key = tuple(pair)
        trigrams.setdefault(key, []).append(follower)

    return trigrams



def build_text():

    trigrams = build_trigrams(words)
    word_pair = list(random.choice(list(trigrams.keys())))
    print (" ".join(word_pair))



if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)

