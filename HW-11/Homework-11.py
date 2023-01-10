# decorator for any function:
def my_new_decorator(func):
    def the_wrapper_around_the_original_function(*args, **kwargs):
        from datetime import datetime
        print(func.__name__, datetime.now().strftime('%H:%M'))
        func(*args, **kwargs)

    return the_wrapper_around_the_original_function


# Custom Exception class:
class MyCustomException(Exception):
    pass


# raise MyCustomException("Custom exception is occured")

# Context manager
class MyWithManag(object):
    def __init__(self, func):
        self.func = func

    def __enter__(self):
        print("=" * 10)

    def __exit__(self, *args, **kwargs):
        print("=" * 10)


s = sum([2, 3, 4, 5])
with MyWithManag(s) as r:
    try:
        print(s)
    except Exception as exp:
        print(exp)

# The same action as previous one
try:
    print('=' * 10)
    s = sum([2, 3, 4, 5])
except Exception as exp:
    print(exp)
else:
    print(s)
finally:
    print('=' * 10)

# HW4
try:
    variable = input('Please, write your value!\n')
    if variable.isdigit():
        print("It's a number", end=' ')
        if int(variable) % 2 == 0:
            print("and even one as well!")
        else:
            print("and odd one as well!")
    else:
         print(f"This is a word! It's length is {len(variable)}")
except Exception as exp:
    print(exp)
