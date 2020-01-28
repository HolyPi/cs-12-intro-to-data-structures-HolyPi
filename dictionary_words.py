import sys as sys
from random import randint
import random

num = int(sys.argv[1])

filename ="/usr/share/dict/words"

mfile = open(filename)

words = mfile.read()

wordslist = words.splitlines()

new_sentence = []

def words():
    for i in range(num):
        random_index = random.randint(0, len(wordslist)-1)
        new_sentence.append(wordslist[random_index])
        wordslist.pop(random_index)


def stringma():
   strings = ''
   for i in range(0, len(new_sentence)):
      strings += new_sentence[i]
      strings += ' '
   return strings

words()
print(stringma())