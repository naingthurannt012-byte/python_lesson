def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

def calculate_average(numbers):
    print("Input numbers:", numbers)
    total = sum(numbers)
    print("Total:", total)
    count = len(numbers)
    print("Count:", count)
    average = total / count
    print("Average:", average)
    return average


import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an informational   message')
logging.warning('This is a warning message')
logging.error('This is an error message')

def calculate_area(length, width):
    assert length > 0, "Length must be positive"
    assert width > 0, "Width must be positive"
    return length * width


with Image.open(image_path) as img:
    # Process the image
    img.close()  # Explicitly close the image file