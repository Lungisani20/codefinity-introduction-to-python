# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold


# Function to calculate revenue
def calculate_revenue(prices, quantities_sold):
    revenue = []
    
    for price, qty in zip(prices, quantities_sold):
        revenue.append(price * qty)
    
    return revenue


# Function to format and print output
def formatted_output(revenues):
    # sort alphabetically by product name (tuple index 0)
    sorted_revenues = sorted(revenues, key=lambda x: x[0])
    
    for product, revenue in sorted_revenues:
        print(f"{product} has total revenue of ${revenue}")


# Calculate revenue per product
revenue_values = calculate_revenue(prices, quantities_sold)

# Combine products with revenue
revenue_per_product = list(zip(products, revenue_values))

# Display results
formatted_output(revenue_per_product)