import math
def calculate_trignometric_values(degrees):
    radians = math.radians(degrees)
    sine = math.sin(radians)
    cosine = math.cos(radians)
    tangent = math.tan(radians)
    return sine , cosine , tangent

degrees = float(input("Enter the angle in degrees: "))
sine , cosine , tangent = calculate_trignometric_values(degrees)
print(f"sin{degrees} = {sine}")
print(f"cos{degrees} = {cosine}")
print(f"tan{degrees} = {tangent}")