def age():
    age = int(input("Please enter the given age: "))
    try:
        age = int(input("Please enter the given age: "))
        print("the age entered by the user:", age)
    except ValueError as ex:
        print("Exception:,Please enter a valid integer value for age.")
    if age % 2 == 0:
        print("The age entered by the user is even.")
    else:
        print("The given age is odd.")
age()
    


