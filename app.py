from flask import Flask
from histogram import histogram, sample

app = Flask(__name__)


@app.route('/')
def generate_words():
    #Build a histogram
    my_histogram = histogram("./text.txt")

    sentence = ""
    num_words = 10
    for i in range(num_words):
        #sample/frequency goes here
        word = sample(my_histogram)
        sentence += " " + word
    return sentence



if __name__ == '__main__':
    app.run()