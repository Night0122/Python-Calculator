def Calculator():

    input = input("Choose out of these 4 operations, Add, Subtract, Multiply, Divide: ")
    
    def Adder():
        x = input("First Number: ")
        y = input("Second Number: ")
        x_int = int(x)
        y_int = int(y)
        xy =  x_int + y_int
        print("Your number is " + str(xy))

    def Subtracter():
        x = input("First Number: ")
        y = input("Second Number: ")
        x_int = int(x)
        y_int = int(y)
        xy =  x_int - y_int
        print("Your number is " + str(xy))

    def Multiplier():
        x = input("First Number: ")
        y = input("Second Number: ")
        x_int = int(x)
        y_int = int(y)
        xy =  x_int * y_int
        print("Your number is " + str(xy))

    def Divider():
        x = input("First Number: ")
        y = input("Second Number: ")
        x_int = int(x)
        y_int = int(y)
        xy =  x_int / y_int
        print("Your number is " + str(xy))

    def Check():
        if input == "Add":
            Adder()
        if input == "Subtract":
            Subtracter()
        if input == "Multiply":
            Multiplier()
        if input == "Divide":
            Divider()
    
    Check()

Calculator()