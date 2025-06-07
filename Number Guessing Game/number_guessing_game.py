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