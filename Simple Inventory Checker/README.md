# Simple Inventory Checker

A Python program that checks if items are available in a predefined inventory list.

## Description

This program allows users to check if their desired items are available in the inventory. It maintains a simple list of available items and checks user input against this list.

## Features

- Input validation for number of items
- Case-insensitive item checking
- Proper error handling for:
  - Invalid number inputs
  - Empty inputs
  - Keyboard interrupts
  - Name errors
  - General exceptions
- Formatted output with capitalized item names
- Continuous prompting until valid input is received

## How to Use

1. Run the program
2. Enter the number of items you want to check
3. Enter each item name when prompted
4. The program will display:
   - Available items from the inventory
   - Unavailable items not found in inventory

## Example Usage

```bash
Enter the number of items (in numbers): 3
1. banana
2. apple
3. orange

Available items:
- Banana
- Apple

Unavailable items:
- Orange
```

## Error Handling

The program handles various error cases:
- Invalid number inputs (non-numeric)
- Empty item names
- Keyboard interrupts (Ctrl+C)
- Other unexpected errors

## How to Run

```python
try:
    inventory = ["banana", "apple"]
    user_list = []

    while True:
        try:
            items_list = int(input("Enter the number of items (in numbers): "))
            if items_list <= 0:
                print("Please enter a positive number")
                continue
            break
            
        except ValueError:
            print("Please enter a valid number")
            continue

    for number in range(1, items_list + 1):
        while True:
            user_item = input(f"{number}. ")
            if user_item:
                user_list.append(user_item.lower())
                break
            else:
                print("Please enter a valid input")
                continue

    available_items = []
    unavailable_items = []

    for items in user_list:
        if items in inventory:
            available_items.append(items)
        else:
            unavailable_items.append(items)
    
    if (available_items):
        print("\nAvailable items:")
        for item in available_items:
            print(f"- {item.capitalize()}")
    if (unavailable_items):
        print("\nUnavailable items:")
        for item in unavailable_items:
            print(f"- {item.capitalize()}")

except KeyboardInterrupt:
    print("\nQuiting")
except NameError:
    print("\nError: Invalid input detected")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
```

## Current Inventory

The program currently checks against these items:
- banana
- apple

## Note

The program is case-insensitive, so "BANANA", "banana", and "Banana" will all match the inventory item "banana".
