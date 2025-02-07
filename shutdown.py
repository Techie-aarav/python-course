def user_input():
    user_input = input("Do you want to shut down your computer ? (Yes/No):")
    if user_input == "Yes":
        print(" shutdown")
    elif user_input == "No":
        print(" abort shutdown")
    else:
        print("sorry")
user_input()