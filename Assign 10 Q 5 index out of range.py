def access_list_element(my_list, index):
    try:
        # Attempt to access the list element at the given index
        element = my_list[index]
        print(f"The element at index {index} is: {element}")
    
    except IndexError:
        print(f"Error: Index {index} is out of range. Please provide a valid index within 0 and {len(my_list) - 1}.")

# Example list
my_list = [10, 20, 30, 40, 50]

# Prompt user for an index to access
index = int(input("Enter the index of the element you want to access: "))
access_list_element(my_list, index)
