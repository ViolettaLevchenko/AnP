k=input("Введите количество слов:   ")
i=1
print("Вводите слова по одному:")
string=""
while i<=int(k):
    word=input()
    string= string + word + " "
    i+=1
print(string)