inventory = []

while True:
    print("\n=== INVENTORY MENU ===")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Find Item")
    print("4. Show Inventory")
    print("5. Exit")

    choice = input("Choose menu (1-5): ")

    if choice == "1":
        item = input("Enter item name to add: ")
        if item not in inventory:
            inventory.append(item)
            print(item, "added to inventory.")
        else:
            print(item, "already exists in inventory.")

    elif choice == "2":
        item = input("Enter item name to remove: ")
        if item in inventory:
            inventory.remove(item)
            print(item, "removed from inventory.")
        else:
            print(item, "not found in inventory.")

    elif choice == "3":
        item = input("Enter item name to find: ")
        if item in inventory:
            print("True")
        else:
            print("False")

    elif choice == "4":
        print("Inventory List:", inventory)

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")

