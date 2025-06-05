# Password Strength Checker

A Python program that evaluates password strength based on length and character types.

## Description

This program checks the strength of passwords by analyzing:
- Password length
- Presence of uppercase letters
- Presence of lowercase letters
- Presence of numbers
- Presence of special characters

## Features

- Password strength evaluation with three levels:
  - Strong: 12+ characters and all character types
  - Moderate: 6+ characters and 3+ character types
  - Weak: Less than 6 characters or fewer character types
- Detailed feedback on missing character types
- Input validation
- Error handling for:
  - Empty inputs
  - Invalid menu choices
  - Keyboard interrupts
  - General exceptions

## How to Use

1. Run the program
2. Choose from the menu:
   - 1: Check Password
   - 2: Exit
3. Enter your password when prompted
4. View the strength assessment and missing requirements

## Example Usage

```bash
--------------------------------------------------
PASSWORD STRENGTH CHECKER
--------------------------------------------------
1. Password Check
2. Exit
--------------------------------------------------
Enter you choice: 1
Enter your password: password123

--------------------------------------------------
Your entered password is WEAK

Missing Items for Strong Password: 
1. UpperCase Letters
2. Special Characters
--------------------------------------------------
```

## Password Requirements

A strong password should have:
- At least 12 characters
- Uppercase letters (A-Z)
- Lowercase letters (a-z)
- Numbers (0-9)
- Special characters (!@#$%^&* etc.)

## How to Run

```python
import string as s

def password_checker(password: str) -> tuple[str, list[str]]:
    missing_elements = []
    pass_len = len(password)

    has_lower = False
    has_upper = False
    has_number = False
    has_special = False

    satisfied_categories = 0

    for char in password:
        if char in s.whitespace:
            return "Not Valid", []
        if char in s.ascii_lowercase:
            has_lower = True
        if char in s.ascii_uppercase:
            has_upper = True
        if char in s.digits:
            has_number = True
        if char in s.punctuation:
            has_special = True

    if has_lower:
        satisfied_categories = satisfied_categories + 1
    if has_upper:
        satisfied_categories = satisfied_categories + 1
    if has_number:
        satisfied_categories = satisfied_categories + 1
    if has_special:
        satisfied_categories = satisfied_categories + 1

    check_case = 1

    if pass_len >= 12 and satisfied_categories >= 4:
        check_case = 3
    elif pass_len >= 6 and satisfied_categories >= 3:
        check_case = 2
    else:
        check_case = 1

    match check_case:
        case 1:
            strength = "weak"
        case 2:
            strength = "moderate"
        case 3:
            strength = "strong"
    
    if not has_upper:
        missing_elements.append("UpperCase Letters")
    if not has_lower:
        missing_elements.append("LowerCase Letters")
    if not has_number:
        missing_elements.append("Numbers")
    if not has_special:
        missing_elements.append("Special Characters")
    
    return strength, missing_elements


def password_checker_body():
    while True:
        user_pass = input("Enter your password: ")
        if user_pass == "":
            print("Please enter a valid password")
            continue

        result, missing_items = password_checker(user_pass)
        print()
        print("-" * 50)
        print(f"Your entered password is {result.upper()}\n")
        
        if result != "Not Valid" and result.lower() != "strong":
            print("Missing Items for Strong Password: ")
            for i, items in enumerate(missing_items, 1):
                print(f"{i}. {items}")
            print("-" * 50)
            print()

        break

def main():
    try:
        while True:
            try:
                print("-" * 50)
                print("Password Strength Checker".upper())
                print("-" * 50)
                print("""
1. Password Check
2. Exit
                    """)
                print("-" * 50)

                user_choice = int(input("Enter you choice: "))
            except ValueError:
                print("Please enter a number")
                continue

            match user_choice:
                case 1:
                    password_checker_body()
                case 2:
                    print("Quiting...")
                    break
                case _:
                    print("Please enter a valid option")
                    continue
    
    except KeyboardInterrupt:
        print("Interupted by user")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

## Note

- The program is case-sensitive
- Spaces are not allowed in passwords
- The program will show which requirements are missing for a strong password
