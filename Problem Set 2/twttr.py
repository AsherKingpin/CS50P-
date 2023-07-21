string = input("INPUT:").strip()
for char in string:
    if char in ("a","e","i","o","u"):
        char = ""
    else:
        print(char,end="")
