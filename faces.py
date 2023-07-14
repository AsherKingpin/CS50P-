def convert(string):
    if string == ":)":
            converted_string = string.replace(":)","😊")
            return converted_string
    if string == ":(":
           converted_string = string.replace(":(","😢")
           return converted_string
    
def main():
        string = input("enter the emoticon:")
        if string == ":)":
                print("the emoji that you wanted is ")
                convert(string)
        if string == ":(":
                print("the emoji that you wanted is")  
                convert(string)      
main()
