# test_calculator.py
import unittest
from calculator import add, multiply

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(100, 200), 300)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(5, 5), 25)

if __name__ == '__main__':
    unittest.main()
