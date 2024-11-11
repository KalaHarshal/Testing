import _thread
import time

# Function to print multiples of a given number
def get_multiple(n):
    i = 1
    print("Multiples of %d:" % n)  # Using old-style string formatting for compatibility
    while i < 11:
        print(i * n)
        i += 1
        time.sleep(0.5)  # Adding delay for readability

# Function to print prime numbers within a range
def get_primes(lower, upper):
    print("\nPrime numbers from %d to %d:" % (lower, upper))  # Old-style string formatting
    primes = []
    for num in range(lower, upper + 1):
        if num <= 1:
            continue
        if num <= 3:
            primes.append(num)
            continue
        if num % 2 == 0 or num % 3 == 0:
            continue
        i = 5
        is_prime = True
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                is_prime = False
                break
            i += 6
        if is_prime:
            primes.append(num)
    print(primes)

# Start the threads
_thread.start_new_thread(get_multiple, (5,))
_thread.start_new_thread(get_primes, (1, 10))

# Keep the main thread alive to let the other threads complete
time.sleep(5)
