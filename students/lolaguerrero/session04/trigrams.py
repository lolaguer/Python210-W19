#!/usr/bin/env python3

# ----------------------------------#
# Assignment: trigrams.py
# Author: Lola Guerrero
# RRoot, 02/03/2019, Created file
# ----------------------------------#

### It needs to be finished, but al least it looks like it works ###

import sys
import random


def read_in_data(file):

    r_file = open(file, 'r')
    text = []
    for line in r_file:
        if line.startswith("**"):
            line = line.replace('\n', '')
        text.append(line)
    return ' '.join(text)



def make_words(text):

    translator = str.maketrans('!"#$%&\'()*+-/:;<=>?@[\\]^_`{|}~', ' '* len('!"#$%&\'()*+-/:;<=>?@[\\]^_`{|}~',))
    return text.translate(translator).split()



def build_trigrams(text):
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



def build_text(word_pairs):

    # Generating the first sentence:
    word_pair = random.choice(list(word_pairs.keys()))
    new_word = random.choice(word_pairs[word_pair])

    # First sentence
    text = " ".join(word_pair + (new_word,))

    for _ in range(len(word_pairs)):

        try:
            word_pair = tuple(text.split()[-2:])
            new_word = random.choice(word_pairs[word_pair])
        except KeyError as e:
            word_pair = random.choice(list(word_pairs.keys()))
            new_word = random.choice(word_pairs[word_pair])

        text += ' ' + new_word

    text = ' '.join(w.capitalize() for w in text.split('. '))

    return text




if __name__ == "__main__":
    # get the filename from the command line
    # try:
    #     filename = sys.argv[1]
    # except IndexError:
    #     print("You must pass in a filename")
    #     sys.exit(1)

    filename = '/Users/i22041/Documents/Python_Certification_UW/PYTHON210/Python210-W19/students/lolaguerrero/session04/sherlock_small.txt'
    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)

    print(new_text)

