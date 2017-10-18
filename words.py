#!/usr/bin/env python3
import argparse
import random
import warnings
import pprint
from collections import Counter

from PyDictionary import PyDictionary

dictionary = PyDictionary()

with open('words.txt', 'r') as f:
    words = [x.strip() for x in f.readlines()]
random.shuffle(words)
words.sort(key=lambda x: len(x), reverse=True)

# Remove this when PyDictionary is fixed
warnings.filterwarnings("ignore")


def get_longest_word(letters: str):
    available_letters = Counter(letters)
    for word in words:
        if len(word) > len(letters):
            continue
        for letter, count in Counter(word).items():
            if letter not in available_letters:
                break
            if count > available_letters[letter]:
                break
        else:
            return word


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('letters', type=str)
    args = parser.parse_args()

    word = get_longest_word(args.letters)
    print(len(word), word)
    pprint.pprint(dictionary.meaning(word))
