expenses = []
monthly_budget = 0

# Allows a user to add an item and an amount to the list of expenses.
def add():
    item = input("Item: ")
    amount = float(input("Amount: $"))
    expenses.append({'item': item, 'amount': amount})
    print(f"Added ${amount} for {item}")

# Tracks each item a user bought and adds up the total of all of them.
def track():
    if not expenses:
        print("You have no expenses yet.")
        return
    print("\n--- Expenses ---")
    total = 0
    for e in expenses:
        print(f"{e['item']}: ${e['amount']}")
        total += e['amount']
    print(f"Total money spent: ${total}")

# Allows a user to create a monthly budget by calculating their monthly salary minus their monthly expenses. They input those expenses manually and they stay until changed again.
def monthly():
    global monthly_budget
    monthly_salary = float(input("What is your monthly salary: $"))
    monthly_expenses = float(input("What are your fixed monthly costs: $"))
    monthly_budget = monthly_salary - monthly_expenses
    print(f"Your monthly budget this month is: ${monthly_budget}")
    return monthly_budget

# Compares the the user's monthly budget by their current expenses and tells them if they are over or under budget.
def compare_budget():
    if monthly_budget == 0:
        print("You must first set your monthly budget.")
        return
    total_spent = sum(e['amount'] for e in expenses)
    print("\n--- Budget Comparison ---")
    print(f"Monthly budget: ${monthly_budget}")
    print(f"Amount spent on items: ${total_spent}")
    if total_spent > monthly_budget:
        print(f"You are over budget by ${total_spent - monthly_budget} this month!")
    else:
        print(f"You are still under budget by ${monthly_budget - total_spent}.")

# Allows a user to clear their expenses at the end of the month.
def clear():
    expenses.clear()
    print("Expenses cleared!")

# This is the mian menu of the Expense Tracker allowing the user to pick what they need to run.
while True:
    print("\n1. Add Item")
    print("2. Track Spending")
    print("3. Enter Monthly Budget")
    print("4. Compare Spending to Budget")
    print("5. Clear")
    print("6. Exit")

    choice = input("Choice: ")

    if choice == '1':
        add()
    elif choice == '2':
        track()
    elif choice == '3':
        monthly()
    elif choice == '4':
        compare_budget()
    elif choice == '5':
        clear()
    elif choice == '6':
        print("Goodbye")
        break
    else:
        print("Invalid choice")