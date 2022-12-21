phone_book = {}
while True:
    commands = input('Write command:\n')
    if commands == 'stats':
        print(f'Amount of records is {len(phone_book)}')
    elif commands == 'list':
        print(*phone_book.keys(), sep='\n')
    elif commands in ['delete', 'show']:
        name = input('Write name:\n')
        if commands == 'delete':
            del phone_book[name]
            print(f'Record with name "{name}" was successfully deleted')
        elif commands == 'show':
            print(f'Here you could see the info for "{name}": {phone_book[name]}')
    elif commands == 'add':
        new_name, phone = input('Provide, please, name and phone:\n').split()
        if new_name in phone_book.keys():
            print(f'Record with {new_name} already exists. Please remove it and add a new one after that')
        else:
            phone_book[new_name] = phone
    elif commands == 'end':
        print('Thanks for your records. Buy!')
        break
    else:
        print(f'There is no such command as "{commands}". Please, try again')
