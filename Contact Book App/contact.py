contacts = {}

while True:
    print('\033[96m\nContact Book App\033[0m')
    print("="*30)
    print('1. Create Contact')
    print('2. View Contact')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contact')
    print('7. Exit')

    choice = input('Enter your choice = ')

    if choice == '1':
        name = input('Enter your name = ')
        if name in contacts:
            print(f'Contact name {name} is already exists!')
        else:
            age = input('Enter age = ')
            email = input('Enter email = ')
            mobile = input('Enter mobile number = ')
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}
            print(f'Contact name {name} has been created successfully!')

    elif choice == '2':
        name = input('Enter contact name to view = ')
        if name in contacts:
            contact = contacts[name]
            print(f'Name: {name}, Age: {age}, Mobile Number: {mobile}')
        else:
            print('Contact not found!')

    elif choice == '3':
        name = input(f'Enter name to updated contact = ')
        if name in contacts:
            age = input('Enter updated age = ')
            email = input('Enter updated email = ')
            mobile = input('Enter updated mobile number = ')
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}
        else:
            print('Contact not found!')

    elif choice == '4':
        name = input('Enter contact name to delete = ')
        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} has been deleted successfully!')
        else:
            print('Contact not found')

    elif choice == '5':
        search_name = input('Enter contact name to search = ')
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found - Name: {name}, Age: {age}, Mobile Number: {mobile}, Email: {email}')
                found = True
        if not found:
            print('No contact found with that name')

    elif choice == '6':
        print(f'Total contacts in your book : {len(contacts)}')

    elif choice == '7':
        print('Good bye...Closing the program')
        break

    else:
        print('Inavlid Input')