variable = input('Please, write your value!\n')
if variable.replace('.', '').isdigit():
    print("It's a number", end=' ')
    if float(variable) % 2 == 0:
        print('and even as well!')
    else:
        print('and odd as well!')
elif isinstance(variable, str):
    print(len(variable))
