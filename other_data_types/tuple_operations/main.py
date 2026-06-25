# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]
# Convert the list to a tuple
shelf1_update_tuple = tuple(shelf1_update)

# Concatenate the tuples
shelf1_concat = shelf1 + shelf1_update_tuple

# Count occurrences of "celery"
celery_count = shelf1_concat.count("celery")

# Find the index of the first occurrence of "celery"
celery_index = shelf1_concat.index("celery")

# Print the results
print("Updated Shelf #1:", shelf1_concat)
print("Number of Celery:", celery_count)
print("Celery Index:", celery_index)