words= input("Enter the words : ")
sorted_unique = sorted(set(words.split()),reverse = True , key = str.lower)
print(" ".join(sorted_unique))
