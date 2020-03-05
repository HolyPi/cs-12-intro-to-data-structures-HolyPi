from flask import Flask
from histogram import histogram, sample
from markov import MarkovChain

app = Flask(__name__)


@app.route('/')
def generate_words():
    #Build a histogram
    my_file = histogram("./text.txt")
    lines = my_file.readlines()
    my_histogram = histogram(lines)
    
    word_list = []
    for line in lines: 
        for word in line.split():
            word_list.append(word)

    sentence = ""
    num_words = 10
    # for i in range(num_words):
    #     #sample/frequency goes here
    #     word = sample(my_histogram)
    #     sentence += " " + word
    # return sentence
    markovchain = MarkovChain(word_list)
    sentence = markovchain.walk(num_words)
    return sentence


if __name__ == '__main__':
    app.run()