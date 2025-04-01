def bilet(n):
    while True:
        try:
            if len(n)%2!=0 or n=="":
                n = input("Некорректный ввод. Попробуйте еще раз. Введите целое число - номер билета. Номер билета должен состоять из четного количества цифр"+ chr(10))
                bilet(n)
            half=int(len(n)/2)
            fhalf=0
            shalf=0
            for i in range(half):
                fhalf+=int(n[i])
                shalf+=int(n[half + i])
            if fhalf==shalf:
                print("Ваш номер счастливый!")
            else:
                print("Ваш номер несчастливый(((")
        except ValueError:
            n=input("Некорректный ввод. Попробуйте еще раз. Введите целое число - номер билета. Номер билета должен состоять из четного количества цифр."+ chr(10))
            bilet(n)
        exit()
bilet(input("Введите номер билета"+ chr(10)))
