import re

# Define the text string and pattern
textstring = ("Wheels on bus go round and round, round and round")
pattern = re.escape("round")

# Find all occurrences of the pattern and their start and end positions
matches = [(match.start(), match.end()) for match in re.finditer(pattern, textstring)]

# Output the results
print ("Substring:", pattern)
print ("Found at Position index of:", matches)
print("Occurrence:", len(matches))
