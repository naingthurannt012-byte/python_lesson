contacts=[]

def exit_program():
    print('Exiting the program. Goodbye!')

def view_contacts():
    print('view contacts')
    for contact in contacts:
        temp=str(contact).split('-')
        print(f"----------")
        print(f"Name: {temp[0]}")
        print(f"Phone: {temp[1]}")
        print(f"Email: {temp[2]}")
        print('----------')

def get_name():
    name=input('enter the name :')
    return name

def get_phone():
    phone=input('enter the phone number :')
    return phone

def get_email():
    email=input('enter the email address :')
    return email

def add_new_contact():
    print('Add New Contact')
    name=get_name()
    phone=get_phone()
    email=get_email()
    new_contact=f"{name}-{phone}-{email}"
    contacts.append(new_contact)
    print('Contact added successfully!')

def del_contact():
    print('Delete Contact')
    name_delete=input('enter the name to delete :') 
    for contact in contacts:
        temp=str(contact).split('-')
        if temp[0]==name_delete:
            contacts.remove(contact)
            print('Contact deleted successfully!')
            return

def get_choice():
    return int(input('Enter your choice (1-4): '))

def Main_menu():
    print(' Contact Manu')
    print('..........................')
    print('[1] View Contacts')
    print('[2] Add New Contact')
    print('[3] Delete Contact')
    print('[4] Exit Program')
    print('..........................')

def main():
    loop = 1
    while loop == 1:
        Main_menu()
        choice = get_choice()
        if choice == 1:
            view_contacts()
        elif choice == 2:
            add_new_contact()
        elif choice == 3:
            del_contact()
        elif choice == 4:
            exit_program()
            loop = 0
        else:
            print('Invalid choice. Please try again.')
if __name__ == '__main__':
    main()

