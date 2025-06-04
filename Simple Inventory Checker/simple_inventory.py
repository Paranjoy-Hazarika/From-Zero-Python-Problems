try:
    inventory = ["banana", "apple"]
    user_list = []

    while True:
        try:
            items_list = int(input("Enter the number of items (in numbers): "))
            if items_list <= 0:
                print("Please enter a positive number")
                continue
            break
            
        except ValueError:
            print("Please enter a valid number")
            continue

    for number in range(1, items_list + 1):
        while True:
            user_item = input(f"{number}. ")
            if user_item:
                user_list.append(user_item.lower())
                break
            else:
                print("Please enter a valid input")
                continue

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
            print(f"- {item.capitalize()}")
    if (unavailable_items):
        print("\nUnavailable items:")
        for item in unavailable_items:
            print(f"- {item.capitalize()}")

except KeyboardInterrupt:
    print("\nQuiting")
except NameError:
    print("\nError: Invalid input detected")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
