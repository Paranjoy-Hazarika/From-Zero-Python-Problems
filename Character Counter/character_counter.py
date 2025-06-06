def character_count(message) -> dict:
    counts = {}

    for i in message.upper():
        if i != " ":
            if i not in counts:
                counts[i] = 0

            counts[i] += 1

    return counts


def main():
    print("CHARACTER COUNTER")
    while True:
        try:
            print("Enter you choice: ")
            print("1. Count Characters")
            print("2. Exit")

            user_choice = int(input("Enter your choice: "))

            match user_choice:
                case 1:
                    while True:
                        message = input("Enter you sentence: ")
                        if message == "":
                            print("Invalid input")
                            continue
                        
                        count_list = character_count(message)

                        for i, (keys, values) in enumerate(count_list.items(), 1):
                            print(f"{i}. {keys} - {values}")
                            
                        break
                case 2:
                    print("Quiting...")
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
            print(f"Error occured: {e}")

        
if __name__ == "__main__":
    main()