# Mini Expense Tracker 

expenses = []   # each entry = {"item": name, "amount": value}

print("Choose one of the following option .")
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spent")
    print("4. Exit")

    choice = input("Enter choice: ")        # Choose any appropriate option you want to execute.
    
    if choice == "1":                       # Condition to be executed if user chooses to "add expenses".
        name = input("Enter item name: ")
        amount = float(input("Enter amount: "))
        expenses.append({"item": name, "amount": amount})
        print("Expenses updated.")

    elif choice == "2":                     # Condition to be executed if user chooses to "view expenses".
        print("\n--- Expenses ---")
        for i in range(len(expenses)):
            print(str(i+1) + ". " + expenses[i]["item"] + " - " + str(expenses[i]["amount"]))

    elif choice == "3":                     # Condition to be executed if user chooses to know "total spent expenses".
        total = 0
        for i in expenses:
            total += i["amount"]
        print("Total spent = " + str(total))

    elif choice == "4":                     # Condition to be executed if user wants to exit the loop.
        print("Thank you")
        break

    else:
        print("Invalid choice!")            # Condition to be executed if user enters an unexpected choice .