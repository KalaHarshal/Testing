# Input list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter with a lambda function to filter even numbers
even_numbers = list(filter(lambda x: x % 3 ==0 , numbers))

# Print the filtered list of even numbers
print(even_numbers)
