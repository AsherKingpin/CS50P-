while True:
    try:
        fuel = (input("Fraction:"))
        x,y = fuel.split("/")
        x = int(x)
        y = int(y)
        percentage = ((x*100)/y)
        if percentage >= 99.0:
            print("F")
        elif percentage <= 1:
            print("E")
        else:
            print(percentage,"%",sep='')

    except ValueError: 
        print("Please Try Again!")
    except ZeroDivisionError:
        print("Y cannot be Zero")
