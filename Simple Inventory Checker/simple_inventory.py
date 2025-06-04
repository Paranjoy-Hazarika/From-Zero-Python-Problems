try:
    inventory = ["banana", "apple"]
    user_list = []

    items_list = int(input("Enter the number of items (in numbers): "))

    for number in range(1, items_list + 1):
        user_item = input(f"{number}. ")
        user_list.append(user_item.lower())

    available_items = []
    unavailable_items = []

    for items in user_list:
        if items in inventory:
            available_items.append(items)
        else:
            unavailable_items.append(items)
    
    if (available_items):
        print("\nAvailable items:")
        for item in available_items:
            print(f"- {item}")
    if (unavailable_items):
        print("\nUnavailable items:")
        for item in unavailable_items:
            print(f"- {item}")

except ValueError:
    print("Error: Please enter a valid number for the list of items")
except NameError:
    print("Error: Invalid input detected")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
