variable = input('Please, write your value!\n')
if variable.replace('.', '').isdigit():
    print("It's a number", end=' ')
    if float(variable) % 2 == 0:
        print("and even one as well!")
    else:
        print("and odd one as well!")
else:
    print(len(variable))
