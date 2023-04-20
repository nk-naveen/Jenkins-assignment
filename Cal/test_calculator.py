import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(4, 2), 2)
        self.assertEqual(calculator.subtract(0, 0), 0)
        self.assertEqual(calculator.subtract(-1, -2), 1)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(0, 5), 0)
        self.assertEqual(calculator.multiply(-1, 5), -5)

    def test_divide(self):
        self.assertEqual(calculator.divide(6, 2), 3)
        self.assertRaises(ValueError, calculator.divide, 6, 0)
        self.assertAlmostEqual(calculator.divide(7, 3), 2.33333333, places=7)

if __name__ == '__main__':
    unittest.main()
