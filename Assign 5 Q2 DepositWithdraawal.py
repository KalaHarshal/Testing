# Initialize the balance to 0
balance = 0

# Read the transaction log inputs from the user
while True:
    transaction = input("Enter transaction (D for deposit, W for withdrawal or 'exit' to stop): ")
    if transaction.lower() == 'exit':
        break
    action, amount = transaction.split()
    amount = int(amount)
    
    if action == 'D':
        balance += amount  # Deposit adds to the balance
    elif action == 'W':
        balance -= amount  # Withdrawal subtracts from the balance

# Output the final balance
print(balance)
