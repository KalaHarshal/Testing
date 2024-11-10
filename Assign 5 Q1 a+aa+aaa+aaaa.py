# Function to calculate the sum of a + aa + aaa + aaaa
def calculate_sum(a):
    # Calculate the sum a + aa + aaa + aaaa
    result = a + int(str(a)*2) + int(str(a)*3) + int(str(a)*4)
    return result

# Read the input digit from the user
a = int(input("Enter a digit: "))

# Call the function and print the result
sum_value = calculate_sum(a)
print(sum_value)
