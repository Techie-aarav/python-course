class Student:
    __SchoolName = "Don bosco school"
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def __display(self):
        print("This is a private method")
std = Student("Jack" , 25)
print(std.name)
print(std.__SchoolName)

