# List of products with their initial stock levels
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

# Shipment received
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]

# Step 1: Subtract units sold
for i in range(len(products)):
    products[i][1] -= units_sold[i][1]

# Step 2: Add shipment received
for i in range(len(products)):
    products[i][1] += shipment_received[i][1]

# Final output
print("Final stock levels for all products:", products)