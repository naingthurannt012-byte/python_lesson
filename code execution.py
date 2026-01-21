x = 0

if x > 5:
    print("x is greater than 5")
  else:  # Incorrect indentation
    print("x is less than or equal to 5")

flag = False
if flag:
    x = 10
    print(x) # No problem here

print(x) # No error if flag = True

value = "Hello"
value[0] = 'h'
print(value)

value = "Hello"
new_value = "h" + value[1:]
print(new_value)  # Output: hello

x = 5
if True:
   x = 10  # You've used 'x' again here!
   print(x)  # Output: 10

print(x)  # Output: 10

x = 10
y = 0
 
result = x / y  # ZeroDivisionError

x = 10
y = 0

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Division by zero")


my_string = ""
lots_of_as = "a" * 1000000000
while True:
    my_string = my_string + lots_of_as  # Add 1 billion "a" characters
