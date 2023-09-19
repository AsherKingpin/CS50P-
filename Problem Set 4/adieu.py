import inflect
p = inflect.engine()
text = ["Adieu","adieu"]

while True:
    try:
        name = input("Name:")
        text.append(name)
    except EOFError:
        print()
        break
    
text[2] = "to " + text[2]

if len(text) == 3:
    final_text = p.join(text,conj='')
    print(final_text)
elif len(text) == 4:
    final_text = p.join(text,final_sep='')
    print(final_text)
else:
    final_text = p.join(text)
    print(final_text)
