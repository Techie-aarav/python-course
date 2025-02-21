class fruit:
    taste1 = "sweet"
    taste2 = "bitter"
    taste3 = "sour"
    def __init__(self,name,color):
        self.name = name
        self.color = color
apple = fruit("Apple" , "Red")
orange = fruit("Orange" , "Orange")
grapes = fruit("Grapes" , "Black")
print(apple.taste1)
print(apple.name , apple.color)
print(orange.taste2)
print(orange.name , orange.color)
print(grapes.taste3)
print(grapes.name , grapes.color)
