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
            
            number = input("Enter your number: ")
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
            print(f"Contact {name} added successfully!")
            break
            
        except ValueError:
            print("Please enter a valid number")
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