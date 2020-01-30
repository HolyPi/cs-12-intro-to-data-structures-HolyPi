
filename ="text.txt"
lines = open(filename, "r")
words = lines.read()

wordslist = words.split()

text_histogram = {}



def histogram():

    for word in wordslist:
        word = word.strip(',)-(?.\"\'!').lower()
        if word not in text_histogram.keys():
            text_histogram[word]= 1 
        else:  
            text_histogram[word] += 1

def unique_words():
    return len(text_histogram)





histogram()
print(text_histogram)
print(unique_words())



