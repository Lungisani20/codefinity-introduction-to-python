prices = [29.99, 45.50, 12.75, 38.20]

for i in range(len(prices)):
    original_price = prices[i]

    # Apply discount based on index
    if i == 0:
        discount = 0.10
    elif i == 1:
        discount = 0.20
    elif i == 2:
        discount = 0.15
    elif i == 3:
        discount = 0.05

    updated_price = original_price * (1 - discount)

    # Update list
    prices[i] = updated_price

    # Print result
    print(f"Updated price for item {i}: ${updated_price:.2f}")