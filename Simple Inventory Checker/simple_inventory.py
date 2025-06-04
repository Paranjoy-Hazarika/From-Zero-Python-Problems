# inventory
# check user requested item in the inventory
# if the items requested are in the list then approve
# give the available items and the unavailable items (if applicable)

inventory = ["banana", "apple"]
user_list = []

items_list = input("Enter the list of items: ")
for number in range(1, int(items_list) + 1):
    user_item = input(f"{number}. ")
    user_list.append(user_item)

available_items = []
unavailable_items = []

for items in user_list:
    if items in inventory:
        available_items.append(items)
    else:
        unavailable_items.append(items)

