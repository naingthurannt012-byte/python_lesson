exam_scores = [55, 70, 78, 52, 68]
curve_amount = 10
# Use a list comprehension to create a new list of curved grades
curved_grades = [score + curve_amount for score in exam_scores]
print("Original scores:", exam_scores)
print("Curved scores:", curved_grades)


grocery_list = ["milk", "hummus", "bread", "cheese", "apples"]
print(len(grocery_list))
print(grocery_list.index("hummus"))
print(grocery_list)
print(grocery_list.append("granola"))
print(grocery_list)
print(grocery_list.remove("bread"))
print(grocery_list)
print(grocery_list.sort())
print(grocery_list)
print(grocery_list.reverse())
print(grocery_list)
print(grocery_list.count("milk"))