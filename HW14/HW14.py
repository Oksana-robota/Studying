import re
import json

# 1
with open('phonebook.txt', 'x+', encoding='utf-8') as phone1:
    try:
        phone_book = json.load(phone1)
    except Exception:
        phone_book = {}

while True:
    commands = input('Write command:\n')
    if commands == 'stats':
        print(f'Amount of records is {len(phone_book)}')
    elif commands == 'list':
        print(*phone_book.keys(), sep='\n')
    elif commands in ['delete', 'show']:
        name = input('Write name:\n')
        if commands == 'delete' and name in phone_book.keys():
            del phone_book[name]
            with open('phonebook.txt', 'w') as ph:
                json.dump(phone_book, ph)
                print(f'Record with name "{name}" was successfully deleted')
        elif commands == 'show' and name in phone_book.keys():
            print(f'Here you could see the info for "{name}": {phone_book[name]}')
        else:
            print(f'There is no such name as {name} in phone book. Firstly, you need to add it!')
    elif commands == 'add':
        new_name, phone = input('Provide, please, name and phone:\n').split()
        if new_name in phone_book.keys():
            print(f'Record with {new_name} already exists. Please remove it and add a new one after that')
        else:
            if re.match(r'\A(\+380|380|0)[0-9]{9}\b', phone):
                with open('phonebook.txt', 'w') as ph:
                    phone_book[new_name] = phone
                    json.dump(phone_book, ph)
                    print(f'Contact "{new_name}" was created in the phone book!')
            else:
                print('This phone number is not valid')
    elif commands == 'end':
        print('Thanks for your records. Buy!')
        break
    else:
        print(f'There is no such command as "{commands}". Please, try again')


# 2
file1 = input('Enter file name\n')
with open(file1, 'r', encoding='utf-8') as file2:
    info1 = file2.readlines()
    for i in info1:
        print(re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '*@*', i), end='')

# 3
file3 = input('Enter file name\n')
with open(file3, 'r', encoding='utf-8') as file4:
    info2 = file4.readlines()
    for i in info2:
        print(re.sub(r'([a-zA-z])([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]+)([a-zA-z])',
                     r'\1****@****\3', i), end='')
