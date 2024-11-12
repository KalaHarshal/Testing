
#Write a Python program that takes two numbers as input from the user and
#performs division. However, you need to handle the Zero Division Error
#exception to ensure that the program does not crash if the user tries to divide by zero. If a Zero Division Error
#occurs, the program should display a meaningful error message and request the user to input the numbers again.




def divide_numbers():
    while True:
        try:
            # Take input from the user
            numerator = float(input("Enter the numerator: "))
            denominator = float(input("Enter the denominator: "))
            
            # Perform division
            result = numerator / denominator
            
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed. Please enter a non-zero denominator.")
        
        except ValueError:
            print("Error: Please enter valid numbers.")
        
        else:
            print(f"The result of the division is: {result}")
            break

# Call the function
divide_numbers()
