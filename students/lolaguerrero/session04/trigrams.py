#!/usr/bin/env python3

# ----------------------------------#
# Assignment: trigrams.py
# Author: Lola Guerrero
# RRoot, 02/03/2019, Created file
# ----------------------------------#


words = 'I wish I may I wish I might'.split()

def find_grams(grams):
    trigram = []
    grams = grams.split()
    for i in range(len(words)):
        for j in range(len(grams)-1):
            if (grams[j] == words[i]) and (grams[j+1] == words[i+1]):
                trigram.append(words[i+2])
    return trigram


# Test
assert find_grams("I wish") == ["I", "I"]
assert find_grams("wish I") == ["may", "might"]
assert find_grams("may I") == ["wish"]
assert find_grams("I may") == ["I"]

trigrams = {}
def build_trigrams(grams):
    #trigrams = {}
    grams = grams.split()
    for i in range(len(words)):
        for j in range(len(grams)-1):
            if (grams[j] == words[i]) and (grams[j+1] == words[i+1]):
                k = tuple(grams)
                if k in trigrams:
                    trigrams[k] += [words[i+2]]
                else:
                    trigrams[k] = [words[i+2]]
    return trigrams


# Test
print (build_trigrams("I wish"))
print (build_trigrams("wish I"))
print (build_trigrams("may I"))
print (build_trigrams("I may"))

assert trigrams == {("I", "wish"): ["I", "I"],
                    ("wish", "I"): ["may", "might"],
                    ("may", "I"): ["wish"],
                    ("I", "may"): ["I"],
                    }

