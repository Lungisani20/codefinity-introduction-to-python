# Create the list
vegetables = ["tomatoes", "potatoes", "onions"]

# Remove "onions"
vegetables.remove("onions")

# Add "carrots" if not already in the list
if "carrots" not in vegetables:
    vegetables.append("carrots")
else:
    print("Carrots are already in the list.")

# Add "cucumbers" if not already in the list
if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
else:
    print("Cucumbers are already in the list.")

# Sort the list alphabetically
vegetables.sort()

# Print the updated inventory
print("Updated Vegetable Inventory:", vegetables)