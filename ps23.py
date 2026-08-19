# Create a dictionary of even numbers from 1 to 20 and their squares
even_squares = {x: x**2 for x in range(1, 21) if x % 2 == 0}
print(even_squares)
