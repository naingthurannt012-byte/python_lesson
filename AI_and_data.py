# # list comprehansion
# import math
# n = int(input("Please enter a positive integer: "))

# factors = [(x, n//x) for x in range(1,round(math.sqrt(n))+1)if n % x == 0]
# print("Factor pairs of", n , ":", factors)


# # round(math.sqrt(n))

# salaries = [350000,600000,450000,800000,280000,1200000]
# high_earners = [salary for salary in salaries if salary > 500000]
# print("High earners:", high_earners)

# salaries = [350000, 600000, 450000, 800000, 280000, 1200000]

# taxes_rate = [salary * 0.05 for salary in salaries if salary > 500000]

# print(f'5% Tax rate : {taxes_rate}')

# city = ("Yangon","Maandalay","Banmaw","Myitkyina",(1,2))
# print(city)

# city = ("Yangon","Maandalay","Banmaw","Myitkyina")
# print(('slicing:',city[::2]))
# print('slicing:',city[::-1])
# print('slicing:',city[:2])

# tup1 = ("Mandalay","Yangon",2000,2005)
# tup2 = (2006,)
# print(type(tup2))
# total_tup = tup1 + tup2
# print(total_tup)
# print(len(total_tup))

# d = {}
# d = dict()
# print(d)
# print(len(d))


# d["name"] = 'fred'
# print(d)
# d["age"] = 22
# print(d)
# print(len(d))


# d_1 = {'John': 44, 'Ella':  39, 'Qwen': 40,'Zoe': 41}
# print(d_1)
# print(d_1['Zoe'])
# d_1['Mg Mg'] = 14
# print(d_1)

# del d_1["Ella"]
# print(d_1)

# # del d_1
# dict_1 ={'name': 'Su Su', 'Age': 10 , 'Class':'Grade 4'}
# dict_1.clear()
# dict_1

# dict_2 = {'name': 'Bo Bo', 'Age' : 12}
# dict_2['age'] = 25
# print(dict_2)

# d = {'John': 44, 'Ella':  39, 'Qwen': 40,'Zoe': 41}

# for k in d.keys():
#     print(k)

# d = {'John': 44, 'Ella':  39, 'Qwen': 40,'Zoe': 41}

# for v in d.values():
#     print(v,end=" ")


# d = {'John': 44, 'Ella':  39, 'Qwen': 40,'Zoe': 41}

# # for key, value in d.items():
#     # print(f"{key}: {value}")
# for item in d.items():
#     print(item)
# print(type(item )) 

# 'John' in d

contacts = {} # The global telephone contact list
running = True
while running:
    command = input('A)dd D)delete L)ook up Q)uit: ')
    if command == 'A' or command == 'a':
        name = input('Enter new name: ')
        number = input('Enter new number: ')
        contacts[name] = number
        print("Contact added successfully!")
    elif command == 'D' or command == 'd':
        name = input('Enter name to delete: ')
        if name in contacts:
            del contacts[name]
            print('Contact deleted successfully!')
        else:
            print('Name not found.')
    elif command == "L" or command == 'l':
        name = input('Enter name to look up: ')
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print('Name not found.')
    elif command == "Q" or command == 'q':
        running = False 