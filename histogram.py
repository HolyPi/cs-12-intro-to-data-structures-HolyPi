
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


histogram()
print(text_histogram)



