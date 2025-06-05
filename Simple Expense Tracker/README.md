# Daily Expense Tracker

A simple Python program to track daily expenses with basic features suitable for beginners.

## Description

This program allows users to track their daily expenses by adding expense entries with amounts and descriptions. It provides a simple interface to view all expenses and calculate the total amount spent.

## Features

- Add expenses with:
  - Amount (with validation for positive numbers)
  - Description
- View all expenses with:
  - Numbered list of expenses
  - Individual expense details
  - Total expense calculation
- Error handling for:
  - Invalid number inputs
  - Negative amounts
  - Empty inputs
  - Keyboard interrupts
  - General exceptions

## How to Use

1. Run the program
2. Choose from the menu options:
   - 1: Add Expenses
   - 2: View Expenses
   - 3: Exit
3. Follow the prompts to:
   - Enter amount (must be positive)
   - Enter description
   - View your expense list

## Example Usage

```bash
----------------------------------------
DAILY EXPENSES TRACKER
----------------------------------------
1. Add Expenses
2. View Expenses
3. Exit
----------------------------------------
Enter your choice: 1
Enter the amount: $25.50
Enter the description: Lunch

----------------------------------------
Overall Expenses
----------------------------------------
1. 25.50 - Lunch
2. 15.00 - Bus fare
----------------------------------------
Total expenses: 40.50
```

## Error Handling

The program handles various error cases:
- Invalid number inputs
- Negative amounts
- Empty inputs
- Keyboard interrupts (Ctrl+C)
- Other unexpected errors

## How to Run

```python
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
```

## Note

- All amounts are stored with 2 decimal places
- The program runs in a loop until explicitly exited
- Use Ctrl+C to terminate the program at any time
