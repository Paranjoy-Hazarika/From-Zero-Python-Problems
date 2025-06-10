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
  - Invalid numbers
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
   - Enter the phone number
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

Enter your choice: 2
1. John: 1234567890
```

## Error Handling

The program handles various error cases:
- Empty name inputs
- Invalid number formats
- Invalid menu choices
- Keyboard interrupts (Ctrl+C)
- Other unexpected errors

## How to Run

```python
def view_contact_list(contacts: dict) -> None:
    for i, (name, number) in enumerate(contacts.items(), 1):
        print(f"{i}. {name}: {number}")

def add_number(contacts: dict) -> None:
    while True:
        try:
            name = input("Enter your name: ")
            if not name:
                print("Please enter a name")
                continue
            
            number = int(input("Enter your number: "))
            if not number:
                print("Please enter a number")
                continue
            
            contacts[name] = number
            break
        except ValueError:
            print("Please enter a number")
        except KeyboardInterrupt:
            print("\nTerminated by user")
            break
        except Exception as e:
            print(f"Error occurred: {e}")

def main():
    contact_list = {}
    print("CONTACT LIST MANAGER")
    
    while True:
        print("MENU")
        print("1. Add Number")
        print("2. View Contact List")
        print("3. Exit")
        try:
            user_choice = int(input("Enter your choice: "))

            match user_choice:
                case 1:
                    add_number(contact_list)
                case 2:
                    view_contact_list(contact_list)
                case 3:
                    print("Quiting...")
                    break
                case _:
                    print("Please enter a valid option (1, 2 or 3)")
                    continue

        except ValueError:
            print("Please enter a number")
        except KeyboardInterrupt:
            print("\nTerminated by user")
            break
        except Exception as e:
            print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
```

## Note

- Contact names must not be empty
- Phone numbers must be valid integers
- Use Ctrl+C to terminate the program at any time
- The contact list is stored in memory and will be cleared when the program exits
