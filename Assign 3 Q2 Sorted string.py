words = input("Enter the words with comma seperated : ")

sorted_words = ",".join(sorted(words.split(","),key = str.lower))

print(sorted_words)
