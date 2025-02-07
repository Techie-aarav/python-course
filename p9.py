def age():
    while True:
        try:
            age = int(input("Please enter the given age: "))
            break
        except ValueError as ex:
            print("Exception: Please enter a valid integer value for age.")
            
    print("The age entered by the user:", age)
    if age % 2 == 0:
        print("The age entered by the user is even.")
    else:
        print("The given age is odd.")
age()