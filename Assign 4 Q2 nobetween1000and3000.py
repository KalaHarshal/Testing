# List to store numbers where each digit is even
x  = int(input("Enter the starting range : "))
y = int (input("Enter the ending range : "))
even_digit_numbers = []

# Iterate through numbers between 1000 and 3000
for num in range(x, y+1):
    # Convert the number to a string and check if all digits are even
    if all(int(digit) % 2 == 0 for digit in str(num)):
        even_digit_numbers.append(str(num))

# Print the result as a comma-separated sequence
print(",".join(even_digit_numbers))

