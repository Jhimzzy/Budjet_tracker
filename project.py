import json

def add_income(transactions):
    type = input("income: ")
    amount = int(input("Whats your income: "))
    category = input("what category: ")
    note = input("Note: ")
    transaction = {"type":type, "category": category, "amount": amount, "note": note}
    transactions.append(transaction)
    print("income added")
    

def add_expense(transactions):
    type = input("expense: ")
    amount = int(input("whats the amount: "))
    category = input("what category: ")
    note = input("Note: ")
    transaction = {"type":type, "category": category, "amount": amount, "note": note}
    transactions.append(transaction)
    print("expense added")


def view_balance(transactions):
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    available = income - expense
    print("available balance:", available)

def view_history (transactions):
    for i in transactions:
        print (i)

def save_to_file(transactions, statement):
    with open(statement,"w") as file:
        json.dump(transactions, file, indent = 4)

def loadfromfile (statement):
    with open(statement,"r") as file:
        transactions = json.load(file)
    return transactions


def main():
    transactions = []
    while True:
      print("1. Add Income")
      print("2. Add Expense")
      print("3. View Balance")
      print("4. View History")
      print("5. Save to File")
      print("6. Load from File")
      print("7. Exit")

      choice = input("choose an option: ")
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
        loadfromfile(transactions)
      elif choice == "7":
        print("bye")
        break
      else:
        print("invalid")

if __name__ == "__main__":
    main()


















































