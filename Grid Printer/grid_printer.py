def get_positive_integer(prompt: str) -> int:
    while True:
        try:
            user_input = int(input(prompt))

            if user_input <= 0:
                print("Please enter a positive integer")
                continue
            return user_input
        except ValueError:
            print("Please enter a valid option")


def print_shape(length: int, height: int):
    print("-" * 50)

    for i in range(1, height + 1):
        for j in range (1, length + 1):
            print("*", end="")

        print("")

    print("-" * 50)


def main():
    print("GRID PRINTER")
    while True:
        try:
            print("Menu:")
            print("1. Rectangle")
            print("2. Square")
            print("3. Exit")

            user_choice = int(input("Enter your choice: "))

            match user_choice:
                case 1:
                    length = get_positive_integer("Enter the length of the grid: ")
                    height = get_positive_integer("Enter the height of the grid: ")
                        
                    print_shape(length, height)
                case 2:
                    side = get_positive_integer("Enter the sides of the square: ")
                        
                    print_shape(side, side)
                case 3:
                    print("Quitting...")
                    break
                case _:
                    print("Please enter a valid option (1, 2 or 3)")
                    continue
        
        except ValueError:
            print("Please enter a valid option")
        except KeyboardInterrupt:
            print("\nTerminated by user")
            break
        except Exception as e:
            print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()