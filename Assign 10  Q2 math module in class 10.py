import math

try:
    # Attempt to call sqrt() with incorrect arguments
    result_sqrt = math.sqrt(16, 2)  # math.sqrt() takes only one argument
    
except TypeError as e:
    print(f"TypeError: {e}")

try:
    # Attempt to call pow() with incorrect arguments
    result_pow = math.pow(2)  # math.pow() requires two arguments
    
except TypeError as e:
    print(f"TypeError: {e}")
