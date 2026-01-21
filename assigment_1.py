# P = eval(input('Enter the principle value : '))
# R = eval(input('Enter the rate interest value:'))
# T = eval(input('Enter the time value :'))
# ci = (P*R*T)/100
# print(f'The compound interest is {ci}')

# a = int(input('enter number '))
# print('The left shift data',a<<5)

# num = 12345
# reverse_num = 0
# # Loop until the original number becomes 0
# while num > 0:
#     digit = num % 10
#     reverse_num = reverse_num * 10 + digit
#     num //= 10

# print(f'The reversed number is {reverse_num}')
# print(f'Original number is {num}')


myan = int(input('Enter your myanmar mark :'))
eng = int(input('Enter your English mark :'))
math = int(input('Enter your math mark :'))
chem = int(input('Enter your chem mark :'))
phy = int(input('Enter your Physis mark :'))
bio = int(input('Enter yor bio mark :'))
subjects =round(((myan+eng+math+chem+phy+bio)/(6*100))*100)
print(f'The average of six subject marks is {subjects} %')


