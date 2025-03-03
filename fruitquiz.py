import random
class fruitQuiz:
    def __init__ (self):
        self.fruits = {"Apple":"red" , "Orange":"orange" , "Grapes":"green" , "Banana" : "yellow"}
    def quiz(self):
        while (True):
            fruit,color = random.choice(list(self.fruits.items()))
            print("What is the color of {}?" . format(fruit))
            user_answer = input()
            if (user_answer.lower() == color):
                print("Correct answer")
            else:
                print("wrong answer")
            option = int(input("Enter 0 , if you want to play again otherwise press 1"))
            if (option):
                break
print("Welcome to fruit quiz")
fq = fruitQuiz()
fq.quiz()


