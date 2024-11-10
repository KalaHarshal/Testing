# Read the input sentence from the user
sentence = input("Enter a sentence: ")

# Initialize counters for capital letters, lowercase letters, and digits
caps = 0
lowercase = 0
digits = 0

# Iterate through each character in the sentence
for char in sentence:
    if char.isupper():
        caps += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digits += 1

# Print the results
print ("CAPS: ", caps)
print ("LOWERCASE: ", lowercase)
print ("DIGITS: ", digits)
