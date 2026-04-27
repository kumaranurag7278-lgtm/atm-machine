def statement(transactions):

    if len(transactions)== 0 :
        print("No transaction yet")
    else:
        print("\n Transaction History:")

        for item in transactions:
            print(item)