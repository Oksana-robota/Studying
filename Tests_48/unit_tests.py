import random
import unittest

def is_odd(number):
    return number % 2 != 0

class TestIsOdd(unittest.TestCase):

    def test_is_odd(self):
        test_odd_number = random.randint(1, 1000000) * 2 - 1
        test_even_number = test_odd_number + 1

        print(f'Testing with odd number: {test_odd_number}')
        self.assertEqual(is_odd(test_odd_number), True, 'Odd number failed')

        print(f'Testing with even number: {test_even_number}')
        self.assertEqual(is_odd(test_even_number), False, 'Even number failed')

if __name__ == '__main__':
    unittest.main()