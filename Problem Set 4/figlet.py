import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

font_list = figlet.getFonts()

if len(sys.argv) == 1:
    selected_font = random.choice(font_list)
    figlet.setFont(font=selected_font)

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "-font": 
        if sys.argv[2] in font_list:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid font name")
    else:
        sys.exit("Invalid option")

else:
    sys.exit("Invalid number of arguments")

text = input("Input: ")
print(figlet.renderText(text))
