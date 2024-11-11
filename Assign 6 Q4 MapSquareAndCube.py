# Input list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter with a lambda function to filter even numbers
square_number = list(map(lambda x: x*x , numbers))

cube_number = list(map(lambda x: x*x*x , numbers))


# Print the filtered list of even numbers
print(square_number)
print(cube_number)
