 #def calculate()
 
while(True):
    print()
    try:
        nums = int(input("Сколько цифр вам необходимо посчитать?\n"))
        
        if nums == 0:
             print("Завершение программы")
             exit()
        if nums == 1:
             print("!!!Ошибка ввода!!!")
             
        if nums == 2:
            x = float(input("Введите первую цифру: "))
            y = float(input("Введите вторую цифру: "))
            print()
            operation = int(input(''' Введите операцию, которую хотели бы выполнить:
            1 +
            2 -
            3 *
            4 /
            Нажмите 0, чтобы выйти
            '''))
            if operation ==0:
                print("Завершение программы")
                exit()
            if operation == 1:
                print("Ответ:",x+y)
            if operation == 2:
                print("Ответ:",x-y)
            if operation == 3:
                print("Ответ:",x*y)
            if operation == 4:
                print("Ответ:",x/y)
        if nums == 3:
            x = float(input("Введите первую цифру: "))
            y = float(input("Введите вторую цифру: "))
            z = float(input("Введите третью цифру: "))
            print()
            operation = int(input(''' Введите операцию, которую хотели бы выполнить:
            1 +
            2 -
            3 *
            4 /
            Нажмите 0, чтобы выйти
            '''))
            if operation ==0:
                print("Завершение программы")
                exit()
            if operation == 1:
                print("Ответ:",x+y+z)
            if operation == 2:
                print("Ответ:",x-y-z)
            if operation == 3:
                print("Ответ:",x*y*z)
            if operation == 4:
                print("Ответ:",x/y/z)
        if nums == 4:
            x = float(input("Введите первую цифру: "))
            y = float(input("Введите вторую цифру: "))
            z = float(input("Введите третью цифру: "))
            w = float(input("Введите четвёртую цифру: "))
            print()
            operation = int(input(''' Введите операцию, которую хотели бы выполнить:
            1 +
            2 -
            3 *
            4 /
            Нажмите 0, чтобы выйти
            '''))
            if operation ==0:
                print("Завершение программы")
                exit()
            if operation == 1:
                print("Ответ:",x+y+z+w)
            if operation == 2:
                print("Ответ:",x-y-z-w)
            if operation == 3:
                print("Ответ:",x*y*z*w)
            if operation == 4:
                print("Ответ:",x/y/z/w)
        if nums == 5:
            x = float(input("Введите первую цифру: "))
            y = float(input("Введите вторую цифру: "))
            z = float(input("Введите третью цифру: "))
            w = float(input("Введите четвёртую цифру: "))
            v = float(input("Введите пятую цифру: "))
            print()
            operation = int(input(''' Введите операцию, которую хотели бы выполнить:
            1 +
            2 -
            3 *
            4 /
            Нажмите 0, чтобы выйти
            '''))
            if operation ==0:
                print("Завершение программы")
                exit()
            if operation == 1:
                print("Ответ:",x+y+z+w+v)
            if operation == 2:
                print("Ответ:",x-y-z-w-v)
            if operation == 3:
                print("Ответ:",x*y*z*w*v)
            if operation == 4:
                print("Ответ:",x/y/z/w/v)
        if nums > 5:
            print("!!!Калькулятор считает максимум 5 чисел!!!")
    except(ZeroDivisionError):
         print("!!!Нельзя разделить на ноль!!!")
    except(ValueError):
       print("\n!!!Ошибка ввода!!!\n")
    
    