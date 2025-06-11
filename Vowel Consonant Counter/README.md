# Vowel Consonant Counter

A simple Python program that counts the number of vowels and consonants in a given text.

## Description

This program analyzes text input and counts the number of vowels and consonants, ignoring spaces and punctuation. It provides a user-friendly interface with a menu system and handles various input scenarios gracefully.

## Features

- Text analysis with:
  - Vowel counting
  - Consonant counting
  - Total character counting
  - Case-insensitive processing
- Input validation for:
  - Empty text
  - Menu choices
  - Text format
- Error handling for:
  - Invalid inputs
  - Keyboard interrupts
  - General exceptions

## How to Use

1. Run the program
2. Choose from the menu options:
   - 1: Run the counter
   - 2: Exit
3. If you choose to run the counter:
   - Enter your text
   - View the results showing:
     - Total characters
     - Number of vowels
     - Number of consonants

## Example Usage

```bash
VOWEL CONSONANT COUNTER
==================================================

MENU
--------------------------------------------------
1. Run the counter
2. Exit
--------------------------------------------------
Enter your choice: 1
Enter your sentence: Hello World!

Results:
--------------------------------------------------
Total characters: 10
Vowels: 3
Consonants: 7
--------------------------------------------------
Count completed successfully!
```

## Error Handling

The program handles various error cases:
- Empty text input
- Invalid menu choices
- Non-numeric menu inputs
- Keyboard interrupts (Ctrl+C)
- Other unexpected errors

## How to Run

```python
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
```

## Note

- The program is case-insensitive
- Spaces and punctuation are ignored in the count
- Use Ctrl+C to terminate the program at any time
- The program uses sets for efficient character lookup
