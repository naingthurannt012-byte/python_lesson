pi = 3.14159
def exit():
    print('Thanks for using my program...')

def back():
    print('Back to main menu...')

def display(ans):
    print('The answer is =',ans)

def get_circle_area(radius):
    return pi * radius * radius

def get_circle_circumference(radius):
    return 2 * pi * radius

def get_triangle_area(base,height):
    return 0.5 * base * height

def get_triangle_volume(base,height):
    return (base*height)/3

def circle_circumference():
    radius = float(input('Enter the radius of the circle: '))
    ans = get_circle_circumference(radius)
    display(ans)

def circle_area():
    radius = float(input('Enter the radius of the circle: '))
    ans = get_circle_area(radius)
    display(ans)

def circle():
    loop = 1
    while loop == 1:
        circle_menu()
        choice = get_choice()
        if choice == 1:
            circle_area()
        elif choice == 2:
            circle_circumference()
        elif choice == 3:
            back()
            loop = 0
        else:
            print('Invalid choice. Please try again.')
def triangle():
    loop = 1
    while loop == 1:
        triangle_menu()
        choice = get_choice()
        if choice == 1:
            triangle_area()
        elif choice == 2:
            triangle_volume()
        elif choice == 3:
            back()
            loop = 0
        else:
            print('Invalid choice. Please try again.')
def get_radius():
    return float(input('Enter the radius of the circle: '))
def get_base():
    return float(input('Enter the base of the triangle: '))
def get_height():
    return float(input('Enter the height of the triangle: '))
def triangle_area():
    base = get_base()
    height = get_height()
    ans = get_triangle_area(base,height)
    display(ans)

def triangle_volume():
    base = get_base()
    height = get_height()
    ans = get_triangle_volume(base,height)
    display(ans)

def get_choice():
    return int(input('Enter your choice (1-3): '))

def triangle_menu():
    print(' Triangle Menu')
    print('.................')
    print('[1] Triangle Area')
    print('[2] Triangle Volume')
    print(' --------------')
    print('[3] Back to Main Menu')
    print('.................')

def circle_menu():
    print(' Circle Menu')
    print('.................')
    print('[1] Circle Area')
    print('[2] Circle Circumference')
    print(' --------------')
    print('[3] Back to Main Menu')
    print('.................')

def Main_menu():
    print(' Method Example 2')
    print('.................')
    print('[1] Circle Calculations')
    print('[2] Triangle Calculations')
    print(' --------------')
    print('[3] Exit Program')
    print('.................')

def main():
    loop = 1
    while loop == 1:
        Main_menu()
        choice = get_choice()
        if choice == 1:
            circle()
        elif choice == 2:
            triangle()
        elif choice == 3:
            exit()
            loop = 0
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()



