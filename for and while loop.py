# for i in range(1,11): # This loop prints 1 through 10, not through 11
    # print(i)

number = 1
while number <= 10:
    print(number) 
    number = number + 1

# option = 0
# while option != 4:
#     print("1. Perform action 1")
#     print("2. Perform action 2")
#     print("3. Perform action 3")
#     print("4. Quit")

fruits = ["apple", "banana", "cherry"]
fruit_length = len(fruits)
print(fruit_length)


fruits = ["apple", "banana", "cherry"]
fruits.append("date")

students = ["Alice", "Bob", "Charlie"]
for student in students:
    print("Hello,", student)

students = ["Alice", "Bob", "Charlie"]
for i in range(0,len(students)):
    print("Hello,", students[i])

total = 0
for number in range(1, 101): 
    total += number
    print("The sum is:", total)

numbers = [1, 2, 3, 4, 5]
index = 0

while index < len(numbers):
    if numbers[index] % 2 == 0:
        print(numbers[index])
    index += 1

for i in range(1, 11):
    for j in range(1, 11):
        print(i, "*", j, "=", i * j, end="\t") # Print the equation
    print() # Move to the next line after each row

for i in range(3):
    print(i)
else:
    print("Loop is complete")

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("While loop is complete")