# Create a list and add sample Celsius temperatures to it 
celsius_temperatures = [0,10,25,32,100] # Start with an empty list (do not modify)

# Add the Celsius temperatures to the list
celsius_temperatures = [0,10,25,32,100]

# Create an empty list to store Fahrenheit temperatures
fahrenheit_temperatures = []

# Print both lists (do not modify)
print("Celsius Temperatures:", celsius_temperatures)
print("Fahrenheit Temperatures:", fahrenheit_temperatures) 

# Lists from Step 1 (do not modify)
celsius_temperatures = [0, 10, 25, 32, 100]
fahrenheit_temperatures = [] 

# Convert each Celsius temperature to Fahrenheit
for celsius in celsius_temperatures:  # Start the loop (do not modify this line)
  fahrenheit =(celsius*9/5)+32

  fahrenheit_temperatures.append(fahrenheit)  # Append to the list (do not modify this line)

# Print the results (including the output from Step 1 - do not modify)
print("Celsius Temperatures:", celsius_temperatures)
print("Fahrenheit Temperatures:", fahrenheit_temperatures)