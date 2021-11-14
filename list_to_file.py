wordlist = []
text = ""

for i in range(1, 627):
    with open("for_irish\irish_list_"+str(i)+".txt", encoding='utf-8') as file:
        for line in file:
            text += line
            print(i)


with open('irish_final.txt', 'w', encoding='utf-8') as file:
    file.write(str(text))

print("END")
