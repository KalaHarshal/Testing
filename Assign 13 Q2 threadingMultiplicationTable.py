import threading
import time

# Function to display multiplication table for a given number
def display(num):
    for i in range(1, 11):
        print(f"Multiplication of {num} * {i} = {num * i}")
        time.sleep(0.5)  # Add delay between prints to simulate work

# Creating threads
try:
    t1 = threading.Thread(target=display, args=(5,), name="MyThread1")
    t2 = threading.Thread(target=display, args=(7,), name="MyThread2")

    # Start the threads
    t1.start()
    t2.start()

    # Wait for both threads to complete
    t1.join()
    t2.join()

    print("Done executing!!!")

except Exception as e:
    print(f"An error occurred: {e}")
