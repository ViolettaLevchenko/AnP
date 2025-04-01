
def del100(num):
    while True:
        try:
            result=100/float(num)
            if result.is_integer():
                print("= "+ str(int(result)))
            else:
                print("= "+ str(result))
        except ValueError:
            print("Требуется ввести число")
            del100(input("100 / "))
        except ZeroDivisionError:
            print("Деление на 0?!")
            del100(input("100 / "))
        exit()

del100(input("100 / "))