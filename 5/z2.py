print("Вводите слова по одному. Для того чтобы закончить, введите 'stop'")
word=input()
string=""
while word!="stop":
    string= string + word + " "
    word=input()
print(string)