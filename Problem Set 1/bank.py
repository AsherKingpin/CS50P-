greeting = input("Gretting:").strip().lower()

if greeting.startswith("hello"):
    print("You get $0")
elif greeting.startswith("h"):
    print("You get $20")
else:
    print("You get $100")
