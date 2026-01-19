# Create the dictionary
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

# Check and update price of Eggs
category, price, stock = grocery_inventory["Eggs"]
if price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (category, price - 1, stock)
else:
    print("The price of Eggs is reasonable.")

# Add a new item: Tomatoes
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

# Manage stock for Milk
category, price, stock = grocery_inventory["Milk"]
if stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (category, price, stock + 20)
else:
    print("Milk has sufficient stock.")

# Remove item based on price (Apples)
category, price, stock = grocery_inventory["Apples"]
if price > 2:
    del grocery_inventory["Apples"]
    print("Apples removed from inventory due to high price.")

# Final print
print(f"Updated inventory: {grocery_inventory}")