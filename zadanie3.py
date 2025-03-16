year=input("Введите год для проверки на високосность"+chr(10))
if year.isdigit():
    year=int(year)
    if (year%4==0 and year%100!=0) or (year%400==0):
        print("Год "+ str(year) +" - високосный")
    else:
        print("Это год не високосный")
else:
    print("Некорректный ввод")

