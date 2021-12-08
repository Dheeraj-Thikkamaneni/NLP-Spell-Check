from collections import Counter
import string
import ast
from flask import Flask, jsonify, render_template, request

def read_file_english():
    words_english = []
    for i in range(1, 15):
        with open('english_list_files/english_list_'+str(i)+'.txt', 'r', encoding='utf-8') as file:
            print(i)
            text = ''
            for line in file:
                text += line
                words_english += ast.literal_eval(text)
    return words_english

def read_file_irish():
    words_irish = []
    for i in range(1, 528):
        with open('irish_list_files/irish_list_'+str(i)+'.txt', 'r', encoding='utf-8') as file:
            print(i)
            text = ''
            for line in file:
                text += line
                words_irish += ast.literal_eval(text)
    return words_irish

def split(word):
    return[(word[:i], word[i:]) for i in range(len(word) + 1)]

def delete(word):
    return [l + r[1:] for l, r in split(word) if r]

def swap(word):
    return [l + r[1] + r[0] + r[2:] for l, r in split(word) if len(r) > 1]

def replace(word):
    letters = string.ascii_lowercase
    return [l + c + r[1:] for l, r in split(word) if r for c in letters]

def insert(word):
    letters = string.ascii_lowercase
    return [l + c + r for l, r in split(word) for c in letters]

def level_one_edit(word):
    return set(delete(word) + swap(word) + replace(word) + insert(word))

def level_two_edit(word):
    return set(e2 for e1 in level_one_edit(word) for e2 in level_one_edit(e1))

def correct_spelling(word, text, word_probability):
    suggestions = level_one_edit(word) or level_two_edit(word) or [word]
    best_guesses = [w for w in suggestions if w in text]
    return [(w, word_probability[w]) for w in best_guesses]

words_english = read_file_english()
each_word_count_english = Counter(words_english)
unique_words_english = set(words_english)
total_word_count_english = float(sum(each_word_count_english.values()))
word_probability_english = {word: (each_word_count_english[word] / total_word_count_english)*1000000 for word in each_word_count_english.keys()}

words_irish = read_file_irish()
each_word_count_irish = Counter(words_irish)
unique_words_irish = set(words_irish)
total_word_count_irish = float(sum(each_word_count_irish.values()))
word_probability_irish = {word: (each_word_count_irish[word] / total_word_count_irish)*1000000 for word in each_word_count_irish.keys()}

unique_words = unique_words_english
word_probability = word_probability_english

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def check():
    if request.method == "POST":
        word = ''
        word = request.form['wrongwords']
        word = word.strip().split()
        word = word[-1]
        guesses = []
        r = []


        language = request.form['language']

        if language == 'irish':
            unique_words = unique_words_irish
            word_probability = word_probability_irish
        elif language == 'english':
            unique_words = unique_words_english
            word_probability = word_probability_english

        
        guesses = correct_spelling(word, unique_words, word_probability)
        toporder_guesses = sorted(guesses, key=lambda x: x[1], reverse=True)[:len(guesses)]  # arranging suggestions in decreasing probability order
        length_of_guesses = len(toporder_guesses)

        k = 0
        flag = 0
        red_flag = 0 # if red_flag = 1 in below code, then the word should be marked as wrong in JS,
        final_guesses = []
        
        for i in range(length_of_guesses):
            if toporder_guesses[i][0] == word:
                k=i
                flag=1
                break

        if flag==1 :
            for i in range(0, length_of_guesses):
                if (toporder_guesses[i][1] > toporder_guesses[k][1]*1000):
                    final_guesses.append(toporder_guesses[i])
            if final_guesses==[]:
                r.append(word) 
                res = " "
                res = res.join(r)
            else:    
                red_flag = 1
                correct_word, num = map(list, zip(*final_guesses)) # breaking guesses list to 2 lists
                r.append(correct_word[0])
                res = " "
                res = res.join(r)
                final_guesses = correct_word

        elif (flag==0 and len(guesses)!=0):
            red_flag = 1
            correct_word, num = map(list, zip(*toporder_guesses)) # breaking guesses list to 2 lists
            r.append(correct_word[0])
            res = " "
            res = res.join(r)
            final_guesses = correct_word

        else:
            r.append(word)
            res = " "
            res = res.join(r)    

        final_suggeestions = ""
        for i in final_guesses:
            final_suggeestions += i+" "
        final_suggeestions = final_suggeestions.strip()

        return jsonify({'final_suggestions': final_suggeestions, 'red_flag': red_flag})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
