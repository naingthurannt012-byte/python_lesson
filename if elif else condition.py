print(' Conditional Statement ')
print(' Finding the largest numbers ')
print(' Algorithm-1 ')
num1=int(input('Enter Num1:'))
num2=int(input('Enter Num2:'))
num3=int(input('Enter Num3:'))
if num1 > num2:
    L=num1
else:
    L=num2
if num3 > L:
    L=num3
print('The largest number is:',L)


if num1>num2 and num1>num3:
    L=num1
elif num2>num1 and num2>num3:
    L=num2
else:
    L=num3
print('The largest number is:',L)