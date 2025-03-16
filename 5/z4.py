import random
import os
errors=0
k=0
print("МАТЕМАТИКА ДЛЯ ДЕТЕЙ"+chr(10)+"Решите примеры:")
while errors<3:
    f=random.randint(0,100)
    s=random.randint(0,100)
    i=int(input(str(f)+" + "+str(s)+" = "))
    if i==f+s:
        print("Правильно!")
        k+=1
    else:
        print("Ответ не верный(((")
        errors+=1
print("Игра окончена. Правильных ответов: "+str(k))
