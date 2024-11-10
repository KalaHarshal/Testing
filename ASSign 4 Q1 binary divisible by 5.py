# Read the comma-separated binary numbers from the user
binary_numbers = input("Enter a sequence of comma-separated 4-digit binary numbers: ")

# Split the input into a list of binary numbers
binary_list = binary_numbers.split(",")

# List to store binary numbers divisible by 5
divisible_by_5 = []

# Check each binary number
for binary in binary_list:
    # Convert binary to decimal
    decimal = int(binary, 2)
    
    # Check if the decimal number is divisible by 5
    if decimal % 5 == 0:
        divisible_by_5.append(binary)

# Print the binary numbers divisible by 5 in a comma-separated sequence
print(",".join(divisible_by_5))
