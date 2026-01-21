def exit():
    print('Thanks for using my program...')
def display(ans):
    print('The answer is =',ans)

def add_num(num1,num2):
    return num1+num2

def sub_num(num1,num2):
    return num1-num2

def multiply_num(num1,num2):
    return num1*num2

def divide_num(num1,num2):
    return num1/num2

def get_input():
    return int(input('Enter a number: '))

def add():
    x = get_input()
    y = get_input()

    ans = add_num(x,y)
    display(ans)

def sub():
    x = get_input()
    y = get_input()

    ans = sub_num(x,y)
    display(ans)

def multiply():
    x = get_input()
    y = get_input()

    ans = multiply_num(x,y)
    display(ans)

def divide():
    x = get_input()
    y = get_input()

    ans = divide_num(x,y)
    display(ans)

def get_choice():
    return int(input('Enter your choice (1-5): '))

def menu():
    print(' Method Example 1')
    print('.................')
    print('[1] Add numbers')
    print('[2] Subtract numbers')
    print('[3] Multiply numbers')
    print('[4] Divide numbers')
    print(' --------------')
    print('[5] Exit Program')
    print('.................')


def main():
    loop = True
    while loop:
        menu()
        choice = get_choice()
        if choice == 1:
            add()
        elif choice == 2:
            sub()
        elif choice == 3:
            multiply()
        elif choice == 4:
            divide()
        elif choice == 5:
            exit()
            loop = False
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()