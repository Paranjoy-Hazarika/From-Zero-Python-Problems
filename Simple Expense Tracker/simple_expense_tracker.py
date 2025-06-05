def add_expense(expenses):
    while True:
        try:
            amount = float(input("Enter the amount: $"))
            if (amount < 0):
                print("Please enter a positive number")
                continue
            description = input("Enter the description: ")

            expense = {
                "amount" : amount,
                "description" : description
            }

            expenses.append(expense)
            break
        
        except ValueError:
            print("Please enter a valid number")
            continue

def view_expenses(expenses):
    total = 0
    try:
        if not expenses:
            print("No expenses added...")
            return

        print("Overall Expenses")
        print("-" * 40)

        for key, values in enumerate(expenses, 1):
            print(f"{key}. {values['amount']:.2f} - {values['description']}")
            total += values['amount']
        
        print("-" * 40)
        print(f"Total expenses: {total:.2f}")
    
    except Exception as e:
        print(f"Error occured: {e}")


def main():
    try:
        print("-" * 40)
        print("DAILY EXPENSES TRACKER")
        overall_expenses = []

        while True:
            print("-" * 40)
            print("""
            1. Add Expenses
            2. View Expenses
            3. Exit
            """)
            print("-" * 40)

            try:
                user_choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a valid number")
                continue

            print()
            match user_choice:
                case 1:
                    add_expense(overall_expenses)
                case 2:
                    view_expenses(overall_expenses)
                case 3:
                    print("Quiting...")
                    quit()
                case _:
                    print("Please enter a valid option")
                    continue
    
    except KeyboardInterrupt:
        print("\nTerminated by user")
    except Exception as e:
        print(f"Error occured: {e}")

if __name__ == "__main__":
    main()