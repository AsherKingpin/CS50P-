grocery = {

}
try:
    while True:
        item = input("Enter the items:").strip().title().upper()
        if item in grocery:
             grocery[item] += 1
        else :
             grocery[item] = 1
except EOFError:
         print("\nYour grocery list:")
         for item, count in sorted(grocery.items()):
            print(f"{count} {item}")
except KeyError:
     pass

