alphabet={}
o=["авеинорст","дклмпу","бгёья","йы","жзхцч","шэю","фщъ"]
for a in range(5):
    for i in o[a]:
        alphabet[i]=a+1
for i in o[5]:
    alphabet[i]=8
for i in o[6]:
    alphabet[i]=10

word=input("Введите слово: ")
score=0
for i in word:
    try:
        score = score + int(alphabet[i])
    except KeyError:
        print("Ошибка. Это не слово")
        exit()
print("Стоимость вашего слова - "+str(score))
