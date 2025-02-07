exp_dict = {"Aarav":2 , "Tennis":2 , "Codingal":3 , "India":2 , "Nepal":4 , "Delhi":2 , "Bombay":2}
print("The orignal dictionary :" + str(exp_dict))
a = 2
count = 0
for key in exp_dict:
    if exp_dict[key] == a:
        count = count + 1
print("Frequency of a is : "+ str(count))