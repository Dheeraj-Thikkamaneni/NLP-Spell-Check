import numpy as np
import pandas as pd
import re # Regular Expressions
from collections import Counter
import string
import enchant

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.readlines()
        words = []
        
        for line in text:
            words = words + re.findall(r'\w+', line.lower()) # RE for making a words list from file
            
    return words        
        
 # edit operations,    insert, delete, swap, replace

def split(word):
    return[(word[:i], word[i:]) for i in range(len(word) + 1)] 
  
def delete(word):
    return [l + r[1:] for l,r in split(word) if r] # l,r left, right for above  
  
# all the above words printed will be suggested, but we need only valid words that in the textfile

def swap(word):
    return [l + r[1] + r[0] + r[2:] for l,r in split(word) if len(r)>1]
  
def replace(word):
    letters = string.ascii_lowercase
    return [l + c + r[1:] for l,r in split(word) if r for c in letters]
  
def insert(word):
    letters = string.ascii_lowercase
    return [l + c + r for l,r in split(word) for c in letters]  


def level_one_edit(word): # perform all operations
    return set(delete(word) + swap(word) + replace(word) + insert(word))

def level_two_edit(word):
    return set(e2 for e1 in level_one_edit(word) for e2 in level_one_edit(e1))

def correct_spelling(word, text, word_probability):
    guesses =[]
    if word in text:
        #print(word)
        return guesses
    
    suggestions = level_one_edit(word) or level_two_edit(word) or [word]
    best_guesses = [w for w in suggestions if w in text]
    return [(w, word_probability[w]) for w in best_guesses]


my_dict = enchant.Dict("en_US")
words = read_file("text.txt") # not as same as above words list
unique_words = set(words)
word_count = Counter(words) # words_count is a dictionary, counts number of each word occurence and stores in dictionary, eg: 'the':613
total_word_count = float(sum(word_count.values())) # values return value in dictionary
word_probability = { word: word_count[word] / total_word_count for word in word_count.keys()} # dict comprehension, word stores each word probability


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['post'])
def check():
    text = request.form['takeinput']
    iwords = text.strip().lower().split()
    guesses = []
    r = []

    for word in iwords:
        guesses = correct_spelling(word, unique_words, word_probability)   # guesses contain a word and its probability
        if len(guesses) != 0:
            cor_word, num = map(list, zip(*guesses))  # breaking guesses list to 2 lists
            n = num.index(max(num))      # finding index of max probability
            r.append(cor_word[n])
        else:
            r.append(word)

        res = " "
        res = res.join(r)

    return render_template('index.html', result=res)



if __name__ == '__main__':
    app.run(debug=True)
