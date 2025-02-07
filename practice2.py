base = float(input("Enter the value of base: "))
exponent = int(input("Enter the value of exponent (non-negative integer only):  "))
#Initial value
value = 1
if exponent >=0:
    for i in range(exponent):
        value *= base
    print(f"{base} raised to power of {exponent} is: {value}")
else:
    print("Please enter a non negative integer for the exponent : ")





