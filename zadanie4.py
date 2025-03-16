print("Выберите два основных цвета (красный, синий, желтый) для смешивания")
first=""
second=""
while first=="":
    first = input("Первый цвет: ")
    if not(first in "красный синий желтый"):
        print("Выберите ОСНОВНОЙ цвет (красный, синий, желтый)")
        first=""
while second=="":
    second = input("Второй цвет: ")
    if not(second in "красный синий желтый"):
        print("Выберите ОСНОВНОЙ цвет (красный, синий, желтый)")
        second=""
if first=="красный" and second=="красный":
    print("Вы получили КРАСНЫЙ")
elif first=="синий" and second=="синий":
    print("Вы получили СИНИЙ")
elif first=="желтый" and second=="желтый":
    print("Вы получили ЖЕЛТЫЙ")
elif (first=="красный" and second=="синий") or (first=="синий" and second=="красный"):
    print("Вы получили ФИОЛЕТОВЫЙ")
elif (first=="синий" and second=="желтый") or (first=="желтый" and second=="синий"):
    print("Вы получили ЗЕЛЕНЫЙ")
elif (first=="красный" and second=="желтый") or (first=="желтый" and second=="красный"):
    print("Вы получили ОРАНЖЕВЫЙ")
