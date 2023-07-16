question = (input("What is the Answer to the Great Question of Life, the Universe, and Everything?"))
question = question.lower()
if question == "42":
    print("yes")
elif question == "forty two":
    print("yes")
elif question == "forty-two":
    print("yes")
else:
    print("no")    

