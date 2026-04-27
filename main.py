from deposite import deposit
from withdraw import withdraw
from record import statement


def ATM():

    balance = 5000
    transactions = []

    while True:

        print("\nMenu")
        print("1. Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Statement")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Current Balance:", balance)

        elif choice == 2:
            balance = withdraw(balance, transactions)

        elif choice == 3:
            balance = deposit(balance, transactions)

        elif choice == 4:
            statement(transactions)

        elif choice == 5:
            print("Thank you")
            break

        else:
            print("Invalid option")

ATM()