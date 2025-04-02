def del3(num):
    while True:
        try:
            if int(num)%3==0:
                print("Да, введенное число делится на 3")
            else:
                print("Нет, введенное число на 3 не делится")
        except ValueError:
            num=input("Некорректное значение. Попробуйте еще раз. Введите целое число."+ chr(10))
            del3(num)
        exit()
del3(input("Введите число для проверки"+chr(10)))
