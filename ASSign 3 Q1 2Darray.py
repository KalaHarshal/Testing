


# Read inputs X and Y from the user
X = int(input("Enter the number of rows (X): "))
Y = int(input("Enter the number of columns (Y): "))

# Generate the 2-dimensional array
array = [[i * j for j in range(Y)] for i in range(X)]

# Print the resulting array
print(array)
