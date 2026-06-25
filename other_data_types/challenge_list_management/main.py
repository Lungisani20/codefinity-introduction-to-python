# Initialize Lists
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

# Create Main List
deli_dept = [meat, cheese, condiment]

# Print initial state
print("Initial Deli List:", deli_dept)

# Restock Item
if "Ham" in meat and meat[2] < 100:
    meat[2] = 100

# Add Seasonal Meat
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

# Remove Condiment
deli_dept.remove(condiment)

# Sort List alphabetically by first element of each sublist
deli_dept.sort(key=lambda item: item[0])

# Print updated state
print("Updated Deli List:", deli_dept)