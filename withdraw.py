def withdraw(balance, transactions):
    amount = int(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient Balance")
    else:
        balance -= amount
        transactions.append(f"Withdrawn {amount}")

    return balance