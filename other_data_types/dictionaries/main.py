# Define the grocery inventory dictionary
grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")
}

# Retrieve details of Bread
bread_details = grocery_inventory["Bread"]
print(f"Details of Bread: {bread_details}")

# Add a new item: Cookies
grocery_inventory["Cookies"] = (143, "Bakery")
print(f"Inventory after adding Cookies: {grocery_inventory}")

# Remove the item: Eggs
grocery_inventory.pop("Eggs")
print(f"Inventory after removing Eggs: {grocery_inventory}")