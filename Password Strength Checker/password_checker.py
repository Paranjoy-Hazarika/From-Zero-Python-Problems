import string as s
import random

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


def generate_password() -> str:
    letters = s.ascii_letters
    digits = s.digits
    special = s.punctuation

    all_chars = letters + digits + special

    password = ""

    for i in range(12):
        password += random.choice(all_chars)

    return password

def main():
    try:
        while True:
            try:
                print("-" * 50)
                print("Password Strength Checker".upper())
                print("-" * 50)
                print("""
1. Password Check
2. Generate Password
3. Exit
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
                    password = generate_password()
                    print(f"\nGenerated Password: {password}")
                case 3:
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
