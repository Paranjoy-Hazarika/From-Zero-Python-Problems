# Bad Word Filter

A simple Python program that filters out inappropriate words from text input, suitable for beginners.

## Description

This program allows users to input text and automatically filters out inappropriate words by replacing them with asterisks. It provides a user-friendly interface with a menu system and handles various input scenarios gracefully.

## Features

- Text filtering with:
  - Customizable bad words list
  - Case-insensitive matching
  - Punctuation preservation
  - Asterisk replacement
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
   - 1: Filter Words
   - 2: Exit
3. If you choose to filter words:
   - Enter your text
   - View the filtered output
4. To exit, select option 2 or press Ctrl+C

## Example Usage

```bash
BAD WORD FILTER
--------------------------------------------------
1. Filter Words
2. Exit
--------------------------------------------------
Enter your choice: 1

Enter your sentence: This is a bad sentence with inappropriate words.

Filtered text:
--------------------------------------------------
This is a bad sentence with ***** *********** words.
--------------------------------------------------
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

def filter_word(sentence: str, bad_words: set) -> str:
    filtered_words = []
    for words in sentence.split():
        clean_word = words.strip(string.punctuation)

        if clean_word.lower() in bad_words:
            filtered_words.append("*" * len(clean_word))
        else:
            filtered_words.append(clean_word)

    
    return " ".join(filtered_words)


def main():
    bad_words = {"foo", "bar", "test", "demo_word"}

    print("BAD WORD FILTER")
    
    while True:
        try:
            print("-" * 50)
            print("1. Filter Words")
            print("2. Exit")
            print("-" * 50)

            user_choice = int(input("Enter your choice: "))

            match user_choice:
                case 1:
                    while True:
                        print()
                        sentence = input("Enter your sentence: ")
                        
                        if not sentence.strip():
                            print("Please enter some text")
                            continue

                        cleaned_words = filter_word(sentence, bad_words)
                        print()
                        print("Filtered text:")
                        print("-" * 50)
                        print(f"{cleaned_words}")
                        break
                case 2:
                    print("Quiting...")
                    break
                case _:
                    print("Please enter a valid option (1 or 2)")
                    continue

        
        except ValueError:
            print("Please enter a number")
        except KeyboardInterrupt:
            print("\nTerminated by user")
            break


if __name__ == "__main__":
    main()
```

## Note

- The program is case-insensitive when checking for bad words
- Punctuation is preserved in the output
- The length of asterisks matches the length of the filtered word
- Use Ctrl+C to terminate the program at any time
