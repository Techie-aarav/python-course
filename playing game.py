import random
playing = True
number = str(random.randint(0,9))
print("I will generate a number from 0 to 9 and you have to guess it. ")
print("The game ends when you get 1 winner! ")
while playing:
    guess = input("Give me your best guess: ")
    if number == guess:
        print("You win the game")
        print("The number was", number)
        break
    else:
        print("Your guess is not right please try again. ")

