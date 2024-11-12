def read_file():
    try:
        # Attempt to open a file
        with open("example.txt", "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print("Error: The file 'example.txt' was not found. Please check the file path and try again.")

# Call the function
read_file()
