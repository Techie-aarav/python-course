character = input("Enter a character: ")
if len(character) == 1:
    ascii_value = ord(character)
    print("The Ascii value of character is: ",ascii_value )
else:
    print("Please enter exactly one character")
    