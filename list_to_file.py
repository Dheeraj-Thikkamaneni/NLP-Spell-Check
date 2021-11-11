wordlist = []
text = ""

for i in range(1, 2):
    with open("english_list_"+str(i)+".txt", encoding='utf-8') as file:
        for line in file:
            text += line


with open('english_final.txt', 'w', encoding='utf-8') as file:
    file.write(str(text))


print("END")
