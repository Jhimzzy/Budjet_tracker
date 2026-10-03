import json 
def add_income(transactions):
    amount = int(input("What's your income: "))
    category = input("What category: ")
    note = input("Note: ")

    transaction = {
        "type": "income",
        "category": category,
        "amount": amount,
        "note": note
    }

    transactions.append(transaction)
    print("Income added")


def add_expense(transactions):
    amount = int(input("What's the amount: "))
    category = input("What category: ")
    note = input("Note: ")

    transaction = {
        "type": "expense",
        "category": category,
        "amount": amount,
        "note": note
    }

    transactions.append(transaction)
    print("Expense added")


def view_balance(transactions):
    income = sum(
        t["amount"] for t in transactions
        if t["type"] == "income"
    )

    expense = sum(
        t["amount"] for t in transactions
        if t["type"] == "expense"
    )

    available = income - expense

    print("Available balance:", available)


def view_history(transactions):
    for transaction in transactions:
        print(transaction)


def save_to_file(transactions, statement="transactions.json"):
    with open(statement, "w") as file:
        json.dump(transactions, file, indent=4)

    print("Transactions saved")


def load_from_file(statement="transactions.json"):
    try:
        with open(statement, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved transactions found")
        return []


def main():
    transactions = []

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View History")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_income(transactions)

        elif choice == "2":
            add_expense(transactions)

        elif choice == "3":
            view_balance(transactions)

        elif choice == "4":
            view_history(transactions)

        elif choice == "5":
            save_to_file(transactions)

        elif choice == "6":
            transactions = load_from_file()

        elif choice == "7":
            print("Bye")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
