# Number Guessing Game

A simple Python program that lets users guess a randomly generated number, suitable for beginners.

## Description

This program generates a random number between 1 and 10, and challenges the user to guess it within 10 attempts. It provides feedback after each guess, indicating whether the guess was too high or too low.

## Features

- Random number generation (1-10)
- Limited attempts (10 tries)
- User feedback with:
  - Number of tries remaining
  - "Too High" or "Too Low" hints
  - Success/failure messages
- Error handling for:
  - Invalid number inputs
  - Out-of-range numbers
  - Keyboard interrupts
  - General exceptions

## How to Use

1. Run the program
2. Choose from the menu options:
   - 1: Play Game
   - 2: Exit
3. Enter your guess (number between 1-10)
4. Follow the hints to guess the number
5. Try to guess the number within 10 attempts

## Example Usage

```bash
NUMBER GUESSING GAME
1. Play Game
2. Exit
Enter your choice: 1

I am thinking of a number between (1 - 10)
Enter your number: 5
Wrong Guess
Tries remaining: 9
TOO LOW

Enter your number: 8
Wrong Guess
Tries remaining: 8
TOO HIGH

Enter your number: 7
OK
Congratulations!!
You guessed it in 3 tries
```

## Error Handling

The program handles various error cases:
- Invalid number inputs (non-numeric)
- Numbers outside the range (1-10)
- Keyboard interrupts (Ctrl+C)
- Other unexpected errors

## How to Run

```python
import random

def number_guesser() -> bool:
    secret_number = random.randint(1, 10)
    overall_tries = 5
    tries = overall_tries
    guessed = False

    print("I am thinking of a number between (1 - 10)")
    print(f"Guess the number. You have {overall_tries} tries")

    while tries != 0:
        try:
            user_number = int(input("Enter your number: "))
            
            if not user_number in range(1, 11):
                print("Please enter a number between 1 - 10")
                continue

            tries -= 1

            if user_number == secret_number:
                print("OK")
                print(f"Congratulations!!\nYou guessed it in {overall_tries - tries} tries")
                guessed = True
                return True
            else:
                print("Wrong Guess")
                print(f"Tries remaining: {tries}")

                if user_number < secret_number:
                    print("TOO LOW")
                else:
                    print("TOO HIGH")
        
        except ValueError:
            print("Please enter a valid number")

    if not guessed:
        print(f"Game Over! The number was {secret_number}")
        return False

def main():
    print("NUMBER GUESSING GAME")

    while True:
        try:
            print("1. Play Game")
            print("2. Exit")

            user_choice = int(input("Enter your choice: "))
            
            match user_choice:
                case 1:
                    number_guesser()
                case 2:
                    print("Quitting...")
                    break
                case _:
                    print("Please enter a valid input (1 or 2)")
        
        except ValueError:
            print("Please enter a number")
        except KeyboardInterrupt:
            print("\nInterrupted by user")
            break
        except Exception as e:
            print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
```

## Note

- The game generates a random number between 1 and 10
- You have 10 attempts to guess the correct number
- The program provides hints after each guess
- Use Ctrl+C to terminate the program at any time
