transactions = []

while True:
    print("\n1. Add Income")
    print("2. Add Transaction (Expense)")
    print("3. View Summary")
    print("4. Exit")

    choice = input("\nEnter choice: ").strip()

    if choice == "4":
        print("Good Bye!")
        break

    elif choice in ("1", "2"):
        try:
            amount = float(input("Amount (₹): "))
            category = input("Category: ").strip()

            t_type = "income" if choice == "1" else "expense"

            transactions.append({
                "type": t_type,
                "amount": amount,
                "category": category
            })

            print(f"✅ Added {t_type} of ₹{amount}")

        except ValueError:
            print("❌ Enter a valid number!")

    elif choice == "3":
        income = sum(t["amount"] for t in transactions if t["type"] == "income")
        expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")

        print(f"\n💚 Income:   ₹{income:.2f}")
        print(f"🔴 Expenses: ₹{expenses:.2f}")
        print(f"💰 Balance:  ₹{income - expenses:.2f}")