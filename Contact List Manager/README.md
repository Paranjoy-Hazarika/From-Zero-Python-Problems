# Contact List Manager

A simple Python program that manages a contact list, allowing users to add and view contacts.

## Description

This program provides a user-friendly interface to manage contacts. It allows users to add new contacts with names and phone numbers, and view the complete contact list in a formatted way. The program includes input validation and error handling to ensure reliable operation.

## Features

- Contact management with:
  - Adding new contacts
  - Viewing contact list
  - Numbered display format
- Input validation for:
  - Empty names
  - Phone number format (7-10 digits)
  - Positive numbers only
  - Digits only
  - Menu choices
- Error handling for:
  - Invalid inputs
  - Keyboard interrupts
  - General exceptions

## How to Use

1. Run the program
2. Choose from the menu options:
   - 1: Add Number
   - 2: View Contact List
   - 3: Exit
3. To add a contact:
   - Enter the contact name
   - Enter the phone number (7-10 digits)
4. To view contacts:
   - Select option 2 to see the complete list

## Example Usage

```bash
CONTACT LIST MANAGER
MENU
1. Add Number
2. View Contact List
3. Exit
Enter your choice: 1

Enter your name: John
Enter your number: 1234567890
Contact John added successfully!

Enter your choice: 2
1. John: 1234567890
```

## Error Handling

The program handles various error cases:
- Empty name inputs
- Invalid number formats:
  - Non-digit characters
  - Numbers less than 7 digits
  - Numbers more than 10 digits
  - Negative numbers
- Invalid menu choices
- Keyboard interrupts (Ctrl+C)
- Other unexpected errors

## How to Run

```python
def view_contact_list(contacts: dict) -> None:
    if not contacts:
        print("\nNo contacts found!")
        return
        
    print("\nContact List:")
    print("-" * 50)
    for i, (name, number) in enumerate(contacts.items(), 1):
        print(f"{i}. {name:<20} | {number}")
    print("-" * 50)

def add_number(contacts: dict) -> None:
    print("\nAdd New Contact")
    print("-" * 50)
    
    while True:
        try:
            name = input("Enter contact name: ")
            if not name:
                print("Name cannot be empty")
                continue
            
            number = input("Enter phone number: ").strip()
            if not number.isdigit():
                print("Number must contain only digits")
                continue
                
            number = int(number)
            if number <= 0:
                print("Number must be positive")
                continue
                
            if len(str(number)) < 7 or len(str(number)) > 10:
                print("Number must be between 7 and 10 digits")
                continue
            
            contacts[name] = number
            print(f"\nContact '{name}' added successfully!")
            break
            
        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user")
            break
        except Exception as e:
            print(f"Error occurred: {e}")

def display_menu() -> None:
    print("\nMENU")
    print("-" * 50)
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")
    print("-" * 50)

def main():
    contact_list = {}
    print("\nCONTACT LIST MANAGER")
    print("-" * 50)
    
    while True:
        display_menu()
        try:
            user_choice = int(input("Enter your choice (1-3): "))

            match user_choice:
                case 1:
                    add_number(contact_list)
                case 2:
                    view_contact_list(contact_list)
                case 3:
                    print("Quiting...")
                    break
                case _:
                    print("\nPlease enter a valid option (1-3)")
                    continue

        except ValueError:
            print("\nPlease enter a number")
        except KeyboardInterrupt:
            print("\nProgram terminated by user")
            break
        except Exception as e:
            print(f"\nError occurred: {e}")


if __name__ == "__main__":
    main()
```

## Note

- Contact names must not be empty
- Phone numbers must:
  - Contain only digits
  - Be positive numbers
  - Be between 7 and 10 digits long
- Use Ctrl+C to terminate the program at any time
- The contact list is stored in memory and will be cleared when the program exits
