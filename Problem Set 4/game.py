import random
while True:
    try:
        n = int(input("enter level:"))
        if n < 0:
              n = int(input("enter level:"))
        break
    except ValueError:
                pass
       
guess_number = random.randint(1,n)

while True:
        try:
            input_number = int(input("Guess:"))
            if  input_number < 0:
                   input_number = int(input("Guess:"))
            else:
                if input_number < guess_number:
                    print("Too small!")
                elif input_number > guess_number:
                    print("Too Big!")
                else:
                    print("Just Right!")
                    break
        except ValueError:
                pass
        except input_number < 0:
               pass
        except EOFError:
               print()
