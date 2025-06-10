number_manager = {
    "Lynn": 8787800327,
    "Lucia": 9730275560
}

while True:
    print("1. Add number")
    print("2. View contact list")

    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        name = input("Enter your name: ")
        number_manager[name] = int(input("Enter the number: "))

    elif user_choice == 2:
        for i, (name, number) in enumerate(number_manager.items(), 1):
            print(f"{i}. {name} - +91{number}")
    else:
        break
