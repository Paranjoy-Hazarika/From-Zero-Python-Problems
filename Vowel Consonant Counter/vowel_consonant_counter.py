import string


def counter(sentence: str) -> None:
    vowels = {"a", "e", "i", "o", "u"}
    consonant = set(string.ascii_lowercase) - vowels

    vowels_count = 0
    consonant_count = 0
    total_chars = 0

    for char in sentence:
        if char != " " and char not in string.punctuation:
            total_chars += 1
            if char in vowels:
                vowels_count += 1
            elif char in consonant:
                consonant_count += 1

    print("\nResults:")
    print("-" * 50)
    print(f"Total characters: {total_chars}")
    print(f"Vowels: {vowels_count}")
    print(f"Consonants: {consonant_count}")
    print("-" * 50)
    print("Count completed successfully!")


def main():
    print("\nVOWEL CONSONANT COUNTER")
    print("=" * 50)
    
    while True:
        print("MENU")
        print("-" * 50)
        print("1. Run the counter")
        print("2. Exit")
        print("-" * 50)
        
        try:
            user_choice = int(input("Enter your choice: "))
            
            match user_choice:
                case 1:
                    while True:
                        sentence = input("Enter your sentence: ")
                        if not sentence:
                            print("Please enter something")
                            continue
                        
                        counter(sentence.lower())
                        break
                    
                case 2:
                    print("Quiting...")
                    break

                case _:
                    print("Please enter a valid option (1 or 2)")
                    continue

        except ValueError:
            print("Please enter a valid input")
        except KeyboardInterrupt:
            print("\nTerminated by the user")
            break
        except Exception as e:
            print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()