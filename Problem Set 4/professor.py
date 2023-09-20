import random


def main():
    level = get_level()
    ca = 0
    for i in range (0,10):
        result_tuple = generate_integer(level)
        number = list(result_tuple)
        answer = int(input(f"{number[0]} + {number[1]} = "))
        sum = number[0] + number[1]
        if sum == answer:
            ca = ca + 1
        else:
            for j in range(0,2):
                print("EEE")
                answer = int(input(f"{number[0]} + {number[1]} = "))
                if answer == sum:
                    break
                if j == 1:
                    print("EEE")
                    print(f"{number[0]} + {number[1]} = {sum}")
    print(f"Score: {ca}")
    

def get_level():
    while True:
        try:
            level = int(input("Enter Level:"))
            if level in (1,2,3):
                return level
                break
            else:
                pass
        except ValueError:
                pass

def generate_integer(level):
    import random
        
    if level == 1:
        number_1 = random.randint(1,9)
        number_2 = random.randint(1,9)
        return number_1, number_2
        
    elif level == 2:
        number_1 = random.randint(10,99)
        number_2 = random.randint(10,99)
        return number_1, number_2

    elif level == 3:
        number_1 = random.randint(100,999)
        number_2 = random.randint(100,999)
        return number_1, number_2

if __name__ == "__main__":
    main()
