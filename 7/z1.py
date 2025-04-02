import random
numbs=[]
for i in range(5):
    numbs.append(random.randint(0,30))
num=""
while num=="":
    num=input("Угадайте число"+chr(10))
    if not num.isdigit():
        print("Некорректный ввод. Попробуйте снова.")
        num=""
if int(num) in numbs:
    print(str(numbs) + chr(10)+ "Ваше число: "+ num +chr(10)+ "Поздравляю, Вы угадали число!")
else:
    print(str(numbs) + chr(10)+ "Ваше число: "+ num +chr(10)+ "Нет такого числа!")