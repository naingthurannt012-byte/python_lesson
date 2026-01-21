# #Find the maximum values
# print('Please enter four integer values.')
# num1 = int(input('enter number 1: '))
# num2 = int(input('enter number 2:'))
# num3 = int(input('enter number 3:'))
# num4 = int(input('Enter number 4:'))
#
# #Compute the maximum value
# if num1 >= num2 and num1 >= num3 and num1 >= num4:
#     max = num1
# elif num2 >= num1 and num2 >= num3 and num2 >= num4:
#     max = num2
# elif num3 >= num1 and num3 >= num2 and num3 >= num4:
#     max = num3
# else:
#     max = num4
# print('The maximun number entered was:',max)
#
# print('Please enter four integer values.')
# num1 = int(input('enter number 1:'))
# num2 = int(input('enter number 2:'))
# num3 = int(input('enter number 3:'))
# num4 = int(input('Enter number 4:'))
# max = num1
# if num2 > max:
#     max = num2
# if num3 > max:
#     max = num3
# if num4 > max:
#     max = num4
# print('The maximum number entered was:',max)


# x = 41
# if 20 <= x <= 40:
#     print(f'{x} is inside')
# else:
#     print(f'{x} is outside')

for i in [1,2,3,4]:
    print('*'*i)

for i in [4,3,2,1]:
    print('*'*i)

for i in range (1,4,1):
    print(i)
    print('Yes'*i)

for i in range(5,0,-1):
    print(i)
    print('*'*i)

for i in range(1,13,1):
    print('The result {}*{} = {}'.format(2,i,i*2))
