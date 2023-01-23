import json
from datetime import datetime

# 1
with open('phonebook.txt', 'r+', encoding='utf-8') as phone1:
    try:
        phone_book = json.load(phone1)
    except Exception:
        phone_book = []

while True:
    commands = input('Write command:\n')
    if commands == 'stats':
        print(f'Amount of records is {len(phone_book)}')
    elif commands == 'list':
        [print(*i.keys(), sep='\n') for i in phone_book]
    elif commands in ['delete', 'show']:
        name = input('Write name:\n')
        keys1 = [s for i in phone_book for s in i.keys()]
        if commands == 'delete' and name in keys1:
            for i in range(len(phone_book)):
                if name in phone_book[i].keys():
                    del phone_book[i]
                    break
            with open('phonebook.txt', 'w') as ph:
                json.dump(phone_book, ph)
                print(f'Record with name "{name}" was successfully deleted')
        elif commands == 'show' and name in keys1:
            for i in phone_book:
                if name in i.keys():
                    print(f'Here you could see the info for "{name}": {i[name]}')
        else:
            print(f'There is no such name as {name} in phone book. Firstly, you need to add it!')
    elif commands == 'add':
        new_name, phone = input('Provide, please, name and phone:\n').split()
        keys1 = [s for i in phone_book for s in i.keys()]
        if new_name in keys1:
            print(f'Record with {new_name} already exists. Please remove it and add a new one after that')
        else:
            with open('phonebook.txt', 'w') as ph:
                phone_book.append({new_name: phone})
                json.dump(phone_book, ph)
                print(f'Contact "{new_name}" was created in the phone book!')
    elif commands == 'end':
        print('Thanks for your records. Buy!')
        break
    else:
        print(f'There is no such command as "{commands}". Please, try again')


# 2
def my_new_decorator(func):
    def the_wrapper_around_the_original_function(*args, **kwargs):
        with open('func1.txt', 'r+') as inf1:
            print(func.__name__, datetime.now().strftime('%H:%M'), file=inf1)
        return func(*args, **kwargs)

    return the_wrapper_around_the_original_function


# 3
class MyCustomException(Exception):
    def __init__(self):
        with open('mistake.txt', 'a') as file1:
            print('Custom exception is occurred at', datetime.now().strftime('%H:%M'), file=file1)


try:
    raise MyCustomException()
except MyCustomException:
    print('The error was noted')
