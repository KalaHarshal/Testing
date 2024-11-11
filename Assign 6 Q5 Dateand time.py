# Take input from user in the format "YYYY-MM-DD HH:MM:SS.mmmmmm"
date_time_str = input("Enter date and time in the format 'YYYY-MM-DD HH:MM:SS.mmmmmm': ")

# Extract year, month, day, and time using lambda functions
extract_year = lambda dt: dt[:4]
extract_month = lambda dt: dt[5:7]
extract_day = lambda dt: dt[8:10]
extract_time = lambda dt: dt[11:19] + "." + dt[20:26]  # Format to 3 decimal places for milliseconds

# Print the extracted values
print(extract_year(date_time_str))
print(extract_month(date_time_str))
print(extract_day(date_time_str))
print(extract_time(date_time_str))



from functools import reduce

# Input date and time as a string
date_time_str = input("Enter date and time in the format 'YYYY-MM-DD HH:MM:SS.mmmmmm': ")

# Use map and lambda to split the string into components
date, time = date_time_str.split()  # Split into date and time parts

# Use map to extract year, month, and day from the date part
year, month, day = map(lambda x: int(x), date.split('-'))

# Use reduce to format time and milliseconds
time_parts = time.split('.')
formatted_time = reduce(lambda x, y: x + "." + y[:3], time_parts)

# Print the extracted values
print(year)
print(month)
print(day)
print(formatted_time)
