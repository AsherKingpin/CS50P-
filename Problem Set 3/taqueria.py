
def total(menu,order_list):
    total = sum(menu[item] for item in order_list)
    return total

def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    order_list = []

    try:
        while True:
            user_input = input("Enter the item from the menu:").strip().title()

            if user_input in menu:
                order_list.append(user_input)
                total_cost = total(menu,order_list)
                print(f"the total cost so far is ${total_cost:.2f}")
            elif user_input == "":
                continue
            else:
                print("Invalid Item chose from the menu")
    except EOFError:
        print("The order is complete")

main()
