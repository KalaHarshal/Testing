def get_numbers():
    try:
        # Prompt user for two numbers
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        # Check if inputs are numerical
        if not (num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit()):
            raise TypeError("Both inputs must be numbers.")
        
        # Convert to float for mathematical operations
        num1 = float(num1)
        num2 = float(num2)
        
        print(f"The numbers you entered are {num1} and {num2}.")
        
    except TypeError as e:
        print(f"TypeError: {e}")

# Call the function
get_numbers()
