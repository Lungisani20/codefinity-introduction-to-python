# Assume start_number is given (example value used here)
start_number = 5

# Step 1: initialize variables
current_number = start_number
countdown_values = []

# Step 2: while loop countdown
while current_number > 0:
    countdown_values.append(current_number)
    current_number -= 1

# Step 3: output results
print("Discount countdown complete!")
print(countdown_values)