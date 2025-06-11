import string


def counter(sentence: str) -> None:
    vowels = {"a", "e", "i", "o", "u"}
    consonant = set(string.ascii_lowercase) - vowels

    vowels_count = 0
    consonant_count = 0

    for char in sentence:
        if char != " " and char not in string.punctuation:
            if char in vowels:
                vowels_count += 1
            elif char in consonant:
                consonant_count += 1

    print(f"Vowels: {vowels_count}")
    print(f"Consonant: {consonant_count}")

def main():
    print("VOWEL CONSONANT COUNTER")

    while True:
        print("MENU")
        print("1. Run the counter")
        print("2. Exit")
        try:
            user_choice = int(input("Enter your choice: "))
            
            match user_choice:
                case 1:
                    sentence = input("Enter your sentence: ")
                    if not sentence:
                        print("Please enter something")
                        continue

                    counter(sentence.lower())
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