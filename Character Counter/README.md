# Character Counter

A simple Python program to count character frequencies in text, suitable for beginners.

## Description

This program analyzes text input and provides a detailed count of each character's frequency. It converts all text to uppercase for consistent counting and excludes spaces and digits from the analysis.

## Features

- Character frequency analysis with:
  - Case-insensitive counting (converts to uppercase)
  - Exclusion of spaces and digits
  - Numbered list output
- Error handling for:
  - Empty inputs
  - Invalid menu choices
  - Keyboard interrupts
  - General exceptions

## How to Use

1. Run the program
2. Choose from the menu options:
   - 1: Count Characters
   - 2: Exit
3. Enter your text when prompted
4. View the character frequency results

## Example Usage

```bash
CHARACTER COUNTER
Menu:
1. Count Characters
2. Exit
Enter your choice: 1
Enter your sentence: Hello World!

1. H - 1
2. E - 1
3. L - 3
4. O - 2
5. W - 1
6. R - 1
7. D - 1
8. ! - 1
```

## Error Handling

The program handles various error cases:
- Empty or whitespace-only inputs
- Invalid menu choices
- Keyboard interrupts (Ctrl+C)
- Other unexpected errors

## How to Run

```python
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
```

## Note

- The program is case-insensitive (converts all text to uppercase)
- Spaces and digits are not counted
- Results are displayed in the order characters appear in the text
- Use Ctrl+C to terminate the program at any time
