print("Numbers with decimals will not be accepted in input, but will be in output, so don't use them in input.")

def Calculator():

    i = input("Choose out of these 4 operations, Add, Subtract, Multiply, Divide: ")
    
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
        if i == "Add":
            Adder()
        if i == "Subtract":
            Subtracter()
        if i == "Multiply":
            Multiplier()
        if i == "Divide":
            Divider()
    
    Check()

    input("Hit Enter to close the program")

Calculator()