import re

count = 0

with open("irish.txt", encoding='utf-8') as file:
    for line in file:
        count = count + 1

print("Number of lines: {}".format(count))

count = 0
text = ""
r = 1
words = []

with open("irish.txt", encoding='utf-8') as file:
    for line in file:
        count = count + 1
        words = words + re.findall("([\w]+[-]?[']?[\w]*)", line, flags=re.IGNORECASE)
        
        files = open('for_irish\irish_list_aa' + str(r) + '.txt', 'w', encoding='utf-8')
        files.write(str(words))
        print(count)
        if count % 5000 == 0:
            r += 1
            words = []
            files.close()

print("END")
