
# imput math

# def calculate_area(radius):
#     return math.pi *radius**2

#     circle_radius = 5
#     area = calculate_area[circle_radius]
#     print(f'The area of the circle with radius {circle_radius}is {area}.')


def calculate_area(length, width):
  area = length * width
  return area

# Example usage:
length = 5
width = 3
rectangle_area = calculate_area(length, width) # Function call, providing inputs
print(f"The area of the rectangle is: {rectangle_area}") # Using the output

def calculate_diameter_circle(radius: float) -> float:
    """
    Calculate the diameter of a circle from its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The diameter of the circle (radius * 2).
               Returns -1 if the radius is negative.
    """
    if radius < 0:
        return -1
    return radius * 2

print(calculate_diameter_circle(7))

global_sum = 0  # Global variable

def calculate_mean_with_side_effect(numbers):
    global global_sum  # Modifying a global variable
    global_sum = sum(numbers)
    return global_sum / len(numbers)

calculate_mean_with_side_effect([5, 3, 4, 1, 1])

def calculate_mean(numbers):
    """Calculates the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

calculate_mean([5, 3, 4, 1, 1])

 
















