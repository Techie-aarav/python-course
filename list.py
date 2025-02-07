empty_list = []
print(empty_list)
numbers = [10,20,30,40,"aarav"]
print(numbers)
squares = [1,4,9]*2
print(squares)
aList = [5,10,15,20]
aList = aList[::-1]
print(aList)

L = [4,5,1,2,9,7,10,8]
print("Orignal list:", L )
count = 0
for i in L:
    count += i
avg = count/len(L)
print("sum = ", count)
print("average = ", avg)
L.sort()
print("Smallest elements is:", L[0])
print("Largest elements is:", L[-1])
