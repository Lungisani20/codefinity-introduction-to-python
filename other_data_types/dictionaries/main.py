# Define the grocery inventory dictionary
grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")
}

# Retrieve Bread details
bread_details = grocery_inventory["Bread"]
print("Details of Bread:", bread_details)

# Add new item Cookies
grocery_inventory["Cookies"] = (143, "Bakery")
print("Inventory after adding Cookies:", grocery_inventory)

# Remove Eggs
del grocery_inventory["Eggs"]
print("Inventory after removing Eggs:", grocery_inventory)