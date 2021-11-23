import re  # Regular Expressions
from collections import Counter
import string
import ast
from flask import Flask, jsonify, render_template, request


def read_file_irish():
    words_irish = []
    for i in range(1, 627):
        with open('irish_list_files\irish_list_'+str(i)+'.txt', 'r', encoding='utf-8') as file:
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

def correct_spelling(word, unique_words, word_probability):
    guesses = []
    if word in unique_words:
        return guesses
    suggestions = level_one_edit(word) or level_two_edit(word) or [word]
    best_guesses = [w for w in suggestions if w in unique_words]
    return [(w, word_probability[w]) for w in best_guesses]

words_irish = read_file_irish()
word_count_irish = Counter(words_irish)
unique_words_irish = set(words_irish)
total_word_count_irish = float(sum(word_count_irish.values()))
word_probability_irish = {word: word_count_irish[word] / total_word_count_irish for word in word_count_irish.keys()}

unique_words = unique_words_irish
word_probability = word_probability_irish


count = 0
text = ''
with open("input-test.txt", encoding='utf-8') as file:
    for line in file:
        count = count + 1
        text+=line
        print(count)

iwords = text.strip().split()
guesses = []
r = []

count = 0
for word in iwords:
    guesses = correct_spelling(word, unique_words, word_probability)
    toporder = sorted(guesses, key=lambda x: x[1], reverse=True)[:len(guesses)]  # arrangoing suggestions in decreasing order
    length = len(toporder)
    if length > 5:
        length = 5

    topfive = sorted(toporder, key=lambda x: x[1], reverse=True)[:length]  # fiding top five suggestions
    if len(topfive) != 0:
        correct_word, num = map(list, zip(*topfive)) # breaking guesses list to 2 lists
        r.append(correct_word[0])
    else:
        r.append(word)
        correct_word = ''

    res = " "
    res = res.join(r)
    print(count)
#print(res)

count = 0
letters = ""
for word in res.split():
    count+=1
    print(count)
    letters += word+"\n"
print("letters are ")    
print(letters)    


file = open('testcases.txt', 'a', encoding='utf-8')
file.write(letters)
        
