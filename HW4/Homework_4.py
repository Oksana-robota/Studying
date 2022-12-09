variable = input('Please, write your value!\n')
if variable.isdigit():
    print("It's a number", end=' ')
    if int(variable) % 2 == 0:
        print("and even one as well!")
    else:
        print("and odd one as well!")
else:
    print(f"This is a word! It's length is {len(variable)}")
