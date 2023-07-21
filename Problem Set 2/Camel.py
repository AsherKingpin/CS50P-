def camel_to_snake(camel_case):
    snake_case = ''
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    return snake_case

def main():
    print("Enter a variable name in camel case:")
    camel_case_input = input()

    snake_case_output = camel_to_snake(camel_case_input)
    print("The variable name in snake case is:", snake_case_output)

if __name__ == "__main__":
    main()

