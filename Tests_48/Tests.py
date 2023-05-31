import random

def is_even(number):
    return number % 2 == 0

def test_is_even():
    test_even_number = random.randint(1, 1000000) * 2
    test_odd_number = test_even_number - 1

    assert is_even(test_odd_number) ==  False, 'Odd number failed'
    assert is_even(test_even_number) == True, 'Even number failed'
    print('Test is_even is ok')

if __name__ == '__main__':
    test_is_even()