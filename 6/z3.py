def magic(date):
    while True:
        try:
            d=date.split(".")
            if (len(d)!=3) or (int(d[0])>31 or int(d[0])<1 or int(d[1])>12 or int(d[1])<1):
                date = input("Неверный формат даты. Попробуйте снова" + chr(10))
                print(magic(date))
            if int(d[0])*int(d[1])==int(d[2][2:]):
                return True
            else:
                return False
        except ValueError:
            date=input("Неверный формат даты. Попробуйте снова"+chr(10))
            print(magic(date))
        except IndexError:
            date=input("Неверный формат даты. Попробуйте снова"+chr(10))
            print(magic(date))
        exit()
print(magic(input("Введите дату в формате дд.мм.гггг"+chr(10))))