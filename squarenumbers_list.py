def find_squares(start , end):
    square_values = [i**2 for i in range (start , end+1)]
    even_squares = [square for square in square_values if square % 2 == 0]
    odd_squares = [square for square in square_values if square % 2 != 0]
    print("Even squares:" , even_squares)
    print("odd squares:" , odd_squares)
find_squares(1, 25)

