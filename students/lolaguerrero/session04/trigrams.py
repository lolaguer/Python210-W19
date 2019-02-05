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
        if line.startswith("**"):
            line = line.replace('\n', '')
        text.append(line)
    return ' '.join(text)



def make_words(text):

    translator = str.maketrans('!"#$%&\'()*+-/:;<=>?@[\\]^_`{|}~', ' ' * len(string.punctuation))
    return text.translate(translator).split()



def build_trigrams(text):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    words = text.split()

    for i in range(len(words) - 2):
        pair = words[i:i + 2]
        follower = words[i + 2]
        key = tuple(pair)
        trigrams.setdefault(key, []).append(follower)

    return trigrams



def build_text():

    in_data = read_in_data("sherlock_small.txt")


    trigrams = build_trigrams(in_data)

    # Generating the first sentence:
    word_pair = random.choice(list(trigrams.keys()))
    new_word = random.choice(trigrams[word_pair])

    # First sentence
    text = " ".join(word_pair + (new_word,))

    for _ in range(len(in_data)):
        word_pair = tuple(text.split()[-2:])
        new_word = random.choice(trigrams[word_pair])
        list_of_words = word_pair + (new_word,)
        new_sentence = " ".join(list_of_words)
        text += new_sentence

    return text




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

