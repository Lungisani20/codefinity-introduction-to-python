# Create the grocery inventory dictionary
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 25),
    "Bread": ("Bakery", 2.00, 15),
    "Apples": ("Produce", 2.50, 20)
}

# Check Eggs price
egg_category, egg_price, egg_stock = grocery_inventory["Eggs"]

if egg_price > 5:
    grocery_inventory["Eggs"] = (egg_category, egg_price - 1, egg_stock)
    print("Eggs are too expensive, reducing the price by $1.")
else:
    print("The price of Eggs is reasonable.")

# Add Tomatoes
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:", grocery_inventory)

# Check Milk stock
milk_category, milk_price, milk_stock = grocery_inventory["Milk"]

if milk_stock < 10:
    milk_stock += 20
    grocery_inventory["Milk"] = (milk_category, milk_price, milk_stock)
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")

# Apples should NOT be removed (fix: only check, do nothing)
apple_category, apple_price, apple_stock = grocery_inventory["Apples"]

if apple_price > 2:
    print("Apples price is high but kept in inventory.")
else:
    print("Apples price is acceptable.")

# Final inventory
print("Updated inventory:", grocery_inventory)