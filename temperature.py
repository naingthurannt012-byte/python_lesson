temperature_c = 25
temperature_f = 77


def celsius_to_fahrenheit(temperature_c):
    fahrenheit = (temperature_c * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(temperature_f):
    celsius = (temperature_f - 32) * 5 / 9
    return celsius


def convert_temperature(temperature, unit):
    if unit == 'C':
        return celsius_to_fahrenheit(temperature)
    elif unit == 'F':
        return fahrenheit_to_celsius(temperature)
    else:
        return "Invalid unit"


# Convert
fahrenheit = convert_temperature(temperature_c, 'C')
celsius = convert_temperature(temperature_f, 'F')

# Print results
print(f"{temperature_c}°C is equal to {fahrenheit}°F")
print(f"{temperature_f}°F is equal to {celsius}°C")
