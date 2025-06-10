number_manager = {
    "Lynn": 8787800327,
    "Lucia": 9730275560
}

name = input("Enter your name: ")
number_manager[name] = int(input("Enter the number: "))

for i, (name, number) in enumerate(number_manager.items(), 1):
    print(f"{i}. {name} - {number}")