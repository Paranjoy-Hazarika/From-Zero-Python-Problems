def character_count(message: str) -> dict:
    counts = {}

    for char in message.upper():
        if char != " " and not char.isdigit():
            if char not in counts:
                counts[char] = 0

            counts[char] += 1

    return counts


def main():
    print("CHARACTER COUNTER")
    while True:
        try:
            print("Menu:")
            print("1. Count Characters")
            print("2. Exit")

            user_choice = int(input("Enter your choice: "))

            match user_choice:
                case 1:
                    while True:
                        message = input("Enter your sentence: ")
                        if not message or message.isspace():
                            print("Invalid input")
                            continue
                        print(message)
                        count_list = character_count(message)

                        for i, (char, count) in enumerate(count_list.items(), 1):
                            print(f"{i}. {char} - {count}")
                            
                        break
                case 2:
                    print("Quitting...")
                    break
                case _:
                    print("Please enter a valid input")
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