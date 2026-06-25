inventory = {
    "Bread": [30, 50, 10, False],   # [stock, min_stock, restock_qty, on_sale]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")

for item, details in inventory.items():
    print(f"Processing {item}")
    
    # Extract values using indexes
    stock = details[0]
    min_stock = details[1]
    restock_qty = details[2]
    on_sale = details[3]
    
    # Restock using while loop
    while stock < min_stock:
        stock += restock_qty
    
    # Update stock back into list
    details[0] = stock
    
    # Apply discount rule
    if stock > discount_threshold and not on_sale:
        details[3] = True

print("Processing completed")