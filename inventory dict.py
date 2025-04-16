# program 3 : Build a simple inventory system where each item and its quantity is stored in a dictionary. Ask the user to enter an item name and quantity to sell.
#Update the dictionary and show the remaining stock or a message if there's not enough.

inventory = {"mobile": 10, "laptop": 15, "mouse": 12}
item = input("Enter the item name to sell: ")
quantity = int(input("Enter the quantity to sell: "))
if item in inventory and inventory[item] >= quantity:
    inventory[item] -= quantity
    print(f"Sold {quantity} {item}(s). Remaining stock: {inventory[item]}")
elif item in inventory:
    print(f"Not enough {item}s in stock. Only {inventory[item]} available.")
else:
    print(f"Item '{item}' not found in inventory.")
print("\nUpdated Inventory:")
for i in inventory:
    print(f"{i.capitalize()}: {inventory[i]}")
