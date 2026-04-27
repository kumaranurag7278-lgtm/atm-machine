def deposit(balance, transactions):
    amount = int(input("Enter amount to deposit: "))

    if amount > 0:
        balance += amount
        transactions.append(f"Deposited {amount}")
    else:
        print("Invalid")

    return balance