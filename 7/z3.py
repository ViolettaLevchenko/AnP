week=("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")
def weekends():
    while True:
        try:
            hope=int(input("Сколько выходных в неделю вы хотите?"+chr(10)))
            if not (hope<=7 and hope>=0):
                print("Некорректный ввод. Попробуйте еще раз.")
                weekends()
            print("Ваши выходные: "+ (", ".join(str(item) for item in week[(7-hope):])) +chr(10)+"Рабочие дни: "+(", ".join(str(item) for item in week[:(7-hope)])))
            exit()
        except ValueError as hope:
            print("Некорректный ввод. Попробуйте еще раз.")
            weekends()
        except IndexError as hope:
            print("Некорректный ввод. Попробуйте еще раз.")
            weekends()
weekends()