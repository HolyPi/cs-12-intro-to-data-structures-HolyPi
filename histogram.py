from random import randint
from random import random

filename = "text.txt"


def histogram(filename):
    lines = open(filename, "r")
    words = lines.read()

    wordslist = words.split()

    text_histogram = {}

    for word in wordslist:
        word = word.strip(',)-(?.\"\'!').lower()
        if word not in text_histogram.keys():
            text_histogram[word]= 1 
        else:  
            text_histogram[word] += 1

    return text_histogram

# def unique_words(histogram):
#     return len(text_histogram)

def sample(histogram):
    tokens = sum([count for word, count in histogram.items()])
    dart = randint(1, tokens)
    fence = 0
    for word, count in histogram.items():
        fence += count
        if fence >= dart:
            return word










print(histogram(filename))
# print(unique_words(text_histogram))