transactions=[]


while True:
    print("\n 1.Add Transactions ")
    print(" 2. Add Incomes")
    print(" 3. View Summary")
    print(" 4. Exit")

    choice=input("\n Enter choice:").strip()


    if choice=="4":
        print("Good Bye!")
        break

if choice in ("1" & "2"):
    try:
        amount = float(input("Amount (rs) :" ))
        category = input("Category: ").strip()
        t_type = "income" if choice == "1" else "expense"

        transactions.append({
            "type" : t_type,
            "amount" : amount,
            "category" : category
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


    