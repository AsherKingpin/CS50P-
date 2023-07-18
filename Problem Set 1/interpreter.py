expression = (input("Expression:").strip())
x, y, z = expression.split(" ")
x = float(x)
z = float(z)
if y == "+":
    total = (x+z)
elif y == "/":
    total = (x/z)
elif y == "*":
    total = (x*z)
elif y == "-":
    total = (x-z)
else:
    print("invaild operator")

print(f"{total:.1f}")
