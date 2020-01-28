import sys as sys
from random import randint
import random


words = sys.argv[1:]

arranged = []


def arrange():
   for i in range(0, len(words)):
      index = random.randint(0, len(words)-1)
      arranged.append(words[index])
      words.pop(index)
      



arrange()
print(arranged)




  


   
