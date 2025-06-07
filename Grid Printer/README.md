# Grid Printer

A simple Python program that prints rectangular and square grids using asterisks, suitable for beginners.

## Description

This program allows users to create and display grids of different sizes. It supports two types of shapes:
- Rectangles with custom length and height
- Squares with equal sides
All shapes are printed using asterisks (*) and are surrounded by a border of dashes.

## Features

- Shape generation with:
  - Rectangle printing with custom dimensions
  - Square printing with equal sides
  - Border decoration
- Input validation for:
  - Positive integers
  - Valid menu choices
  - Number format
- Error handling for:
  - Invalid inputs
  - Keyboard interrupts
  - General exceptions

## How to Use

1. Run the program
2. Choose from the menu options:
   - 1: Rectangle
   - 2: Square
   - 3: Exit
3. For rectangle:
   - Enter the length
   - Enter the height
4. For square:
   - Enter the side length
5. View the generated shape

## Example Usage

```bash
GRID PRINTER
Menu:
1. Rectangle
2. Square
3. Exit
Enter your choice: 1
Enter the length of the grid: 4
Enter the height of the grid: 3

--------------------------------------------------
****
****
****
--------------------------------------------------

Enter your choice: 2
Enter the sides of the square: 3

--------------------------------------------------
***
***
***
--------------------------------------------------
```

## Error Handling

The program handles various error cases:
- Non-positive numbers
- Invalid menu choices
- Non-numeric inputs
- Keyboard interrupts (Ctrl+C)
- Other unexpected errors

## How to Run

```python
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
```

## Note

- All dimensions must be positive integers
- Shapes are printed using asterisks (*)
- Each shape is surrounded by a border of dashes
- Use Ctrl+C to terminate the program at any time
