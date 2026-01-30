shopping_list = ["apples", "bananas", "milk"]  # List for items
item_quantities = {"apples": 3, "bananas": 1}  # Dictionary for quantities

# User adds an item
shopping_list.append("eggs")
item_quantities["eggs"] = 12 

# User increases the quantity of bananas
item_quantities["bananas"] += 2

# User removes apples
shopping_list.remove("apples")
del item_quantities["apples"]

# Print updated list and dictionary
print(shopping_list)
print(item_quantities)

# Tuples
coordinates = (37.7749, -122.4194)  # Latitude, longitude of San Francisco
birth_date = (1990, 12, 25)       # Year, month, day

# Sets
unique_colors = {"red", "green", "blue"}
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)    # Removes duplicates

shopping_cart = []
shopping_cart.extend(["apple","banana","milk"])

print("Shopping Cart:")
for item in shopping_cart:
    print(item)