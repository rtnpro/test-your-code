import unittest
from fizzbuzz import fizzbuzz, main


class TestFizzBuzz(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), 'FizzBuzz')

    def test_other_number(self):
        self.assertEqual(fizzbuzz(2), '2')

    def test_zero_error(self):
        self.assertRaises(ValueError, fizzbuzz, 0)


if __name__ == '__main__':
    unittest.main()
