import ast


def read_file(filename):
    words = []
    text = ""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            text += line

    words = ast.literal_eval(text)
    return words


words = read_file('textbreakt51.txt')  # not as same as above words list
print('words')
print(type(words))
