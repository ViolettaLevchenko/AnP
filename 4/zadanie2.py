seat=input("Введите номер места"+chr(10))
if seat.isdigit():
    seat=int(seat)
    if seat%2==0:
        vn="верхнее"
    else:
        vn="нижнее"
    if seat >= 1 and seat <= 36:
        kb = "в купе"
    elif seat >= 37 and seat <= 54:
        kb = "боковое"
    else:
        print("Некорректный ввод")
        exit()
    print("Ваше место "+vn+" "+kb)
else:
    print("Некорректный ввод")