while(True):
    print()
    try:
        nums = int(input("How many numbers you want to calculate?\n"))
    # x = float(input("Enter the first number: "))
    # y = float(input("Enter the second number: "))
    # z = float(input("Enter the third number: "))
    # w = float(input("Enter the forth number: "))
    # v = float(input("Enter the fifth number: "))

        if nums == 2:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            print()
            func = int(input('''What do you want to do?
            1 to add
            2 to subtract
            3 to multiply
            4 to divide
            '''))
            if func == 1:
                print(x+y)
            if func == 2:
                print(x-y)
            if func == 3:
                print(x*y)
            if func == 4:
                print(x/y)
        if nums == 3:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            z = float(input("Enter the third number: "))
            print()
            func = int(input('''What do you want to do?
            1 to add
            2 to subtract
            3 to multiply
            4 to divide
            '''))
            if func == 1:
                print(x+y+z)
            if func == 2:
                print(x-y-z)
            if func == 3:
                print(x*y*z)
            if func == 4:
                print(x/y/z)
        if nums == 4:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            z = float(input("Enter the third number: "))
            w = float(input("Enter the forth number: "))
            print()
            func = int(input('''What do you want to do?
            1 to add
            2 to subtract
            3 to multiply
            4 to divide
            '''))
            if func == 1:
                print(x+y+z+w)
            if func == 2:
                print(x-y-z-w)
            if func == 3:
                print(x*y*z*w)
            if func == 4:
                print(x/y/z/w)
        if nums == 5:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            z = float(input("Enter the third number: "))
            w = float(input("Enter the forth number: "))
            v = float(input("Enter the fifth number: "))
            print()
            func = int(input('''What do you want to do?
            1 to add
            2 to subtract
            3 to multiply
            4 to divide
            '''))
            if func == 1:
                print(x+y+z+w+v)
            if func == 2:
                print(x-y-z-w-v)
            if func == 3:
                print(x*y*z*w*v)
            if func == 4:
                print(x/y/z/w/v)
        if nums > 5:
            print("The calculator handles 5 numbers maximum!")
    except(ZeroDivisionError):
        print("You can never divide by Zero!")
    except(ValueError):
        print("Check your input.")