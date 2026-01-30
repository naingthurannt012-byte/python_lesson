def calculate_area(width=1, height=1):
    area = width * height
    return area
result = calculate_area() 
print(result)  # Output: 1

result = calculate_area(5, 3)  
print(result)  # Output: 15


def greet(name, greeting="Hello"):
    print(greeting, name)

greet("Alice")  # Output: Hello Alice


greet("Bob", "Good morning")  # Output: Good morning Bob
greet("Carol", "Howdy")      # Output: Howdy Carol

def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="Alice", age=30)


def create_user_profile(name, age, occupation="Student", interests=None): # Use None as default
    """
    Creates a user profile with optional interests.

    Args:
        name (str): The user's name (required).
        age (int): The user's age (required).
        occupation (str, optional): The user's occupation (defaults to "Student").
        interests (list, optional): A list of the user's interests (defaults to None).
    """
    if interests is None:  # Initialize if None
        interests = [] 

    profile = {
        "name": name,
        "age": age,
        "occupation": occupation,
        "interests": interests
    }

    return profile

# Usage
user1 = create_user_profile("Alice", 25, "Software Engineer", ["Coding", "Hiking"])
user2 = create_user_profile("Bob", 18)  # Uses default occupation and no interests
user3 = create_user_profile("Carol", 30, interests=["Gardening", "Reading"])

print(user1)
print(user2)
print(user3)

def make_sandwich(bread_type, filling, cheese="none", toasted=False):
    """
    Create a description of a sandwich based on the given ingredients and options.

    Args:
        bread_type (str): The type of bread used.
        filling (str): The main filling of the sandwich.
        cheese (str, optional): The type of cheese. Defaults to "none".
        toasted (bool, optional): Whether the sandwich is toasted. Defaults to False.

    Returns:
        str: A descriptive sentence about the sandwich.
    """
    if toasted:
        toast_text = "toasted"
    else:
        toast_text = "not toasted"

    return f"You are making a {toast_text} sandwich with {filling} on {bread_type} bread and {cheese} cheese."
