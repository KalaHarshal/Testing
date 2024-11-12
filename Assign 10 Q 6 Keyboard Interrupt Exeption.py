def get_number():
    try:
        # Prompt the user for a number
        number = float(input("Please enter a number: "))
        print(f"You entered: {number}")
    
    except KeyboardInterrupt:
        print("\nInput cancelled by the user.")

# Call the function
get_number()
