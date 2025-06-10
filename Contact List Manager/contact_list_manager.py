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