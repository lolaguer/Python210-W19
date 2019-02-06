#!/usr/bin/env python3

# ----------------------------------#
# Assignment: trigrams.py
# Author: Lola Guerrero
# RRoot, 02/03/2019, Created file
# ----------------------------------#


import sys
import random

## Data ##
def find_start_finish_lines(file):
    """
    Returns the line number of where to start and finish reading a file
    """
    r_file = open(file, 'r')
    for num, line in enumerate(r_file):
        if line.startswith("*** START OF THIS PROJECT"):
            start = num + 1
        if line.startswith("*** END OF THIS PROJECT"):
            finish = num - 1
    return start, finish



def read_in_data(file):
    """
    Reads a file from/to specific lines and processes some of the text in it

    returns a string
    """
    start, finish = find_start_finish_lines(file)
    r_file = open(file, 'r')
    r_file = r_file.readlines()[start:finish]
    text = []
    for line in r_file:
        line = line.replace('\n', ' ')
        line = line.replace(' XII. ', ' ').replace('XII. ', ' ')
        line = line.replace(' XI. ', ' ').replace('XI. ', ' ')
        line = line.replace(' X. ', ' ').replace('X. ', ' ')
        line = line.replace(' IX. ', ' ').replace('IX. ', ' ')
        line = line.replace(' VIII. ', ' ').replace('VIII. ', ' ')
        line = line.replace(' VII. ', ' ').replace('VII. ', ' ')
        line = line.replace(' VI. ', ' ').replace('VI. ', ' ')
        line = line.replace(' V. ', ' ').replace('V. ', ' ')
        line = line.replace(' IV. ', ' ').replace('IV. ', ' ')
        line = line.replace(' III. ', ' ').replace('III. ', ' ')
        line = line.replace(' II. ', ' ').replace('II. ', ' ')
        line = line.replace('I. ', ' ')

        text.append(line.lower())

    text = ' '.join(text)
    text = ' '.join(text.split()).strip() # remove multiple spaces
    return text


def make_words(text):
    """
    Returns a list of words without punctuation (except commas, periods, and tries to keep apostrophe)
    """
    # Removing punctuation
    translator = str.maketrans('!"#$%&()*+-/:;<=>?@[\\]^_`{|}~', ' '* len('!"#$%&()*+-/:;<=>?@[\\]^_`{|}~',))
    text = text.translate(translator)
    # Removing quotation mark
    text = text.replace("' ", " ").replace(" '", " ")
    return text.split()


## Preprocessing ##
def build_trigrams(text):
    """
    Build up the trigrams dict from the list of words

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
    """
    Creates text based on the build_trigrams dict

    returns a string
    """
    # Generating the first sentence:
    word_pair = random.choice(list(word_pairs.keys()))
    new_word = random.choice(word_pairs[word_pair])

    # First sentence
    text = " ".join(word_pair + (new_word,))

    # Add new words based on the two previous ones.
    for _ in range(len(word_pairs)):

        try:
            word_pair = tuple(text.split()[-2:])
            new_word = random.choice(word_pairs[word_pair])
        except KeyError:
            word_pair = random.choice(list(word_pairs.keys()))
            new_word = random.choice(word_pairs[word_pair])

        text += ' ' + new_word

    text = ' '.join('. '+ w.capitalize() for w in text.split('. '))
    text = text.replace(' i ', ' I ')
    text = text.replace(' . ', '. ')
    text = text[2:]+'.'

    return text


if __name__ == "__main__":

    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)

    print(new_text)

