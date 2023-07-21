fruit_calories = {
    "apple": 139,
    "avacado": 50,
    "banana": 110,
    "Cantaloupe": 50,
    "grapefruit": 60,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine":60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine":50, 
    "watermelon":80,
}

def main():
    fruit_input = input("Enter a fruit: ").lower()

    if fruit_input in fruit_calories:
        calories_per_portion = fruit_calories[fruit_input]
        print(f"One portion of {fruit_input} contains {calories_per_portion} calories.")
    else:
        print("Input is not a fruit. Please enter a valid fruit name from the FDA's poster.")

if __name__ == "__main__":
    main()
