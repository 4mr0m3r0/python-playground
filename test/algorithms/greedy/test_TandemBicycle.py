import unittest

from algorithms.greedy.TandemBicycle import TandemBicycle


class MyTestCase(unittest.TestCase):
    def test_given_speeds_when_fastest_true_then_32(self):
        red = [5, 5, 3, 9, 2]
        blue = [3, 6, 7, 2, 1]
        result = TandemBicycle.tandem_bicycle(red, blue, fastest=True)
        self.assertEqual(32, result)

    def test_given_speeds_when_fastest_false_then_25(self):
        red = [5, 5, 3, 9, 2]
        blue = [3, 6, 7, 2, 1]
        result = TandemBicycle.tandem_bicycle(red, blue, fastest=False)
        self.assertEqual(25, result)

    def test_given_speeds_when_fastest_false_then_484(self):
        red = [3, 3, 4, 6, 1, 2, 5, 6, 34, 256, 123, 32]
        blue = [1, 2, 1, 9, 12, 3, 1, 54, 21, 231, 32, 1]
        result = TandemBicycle.tandem_bicycle(red, blue, fastest=False)
        self.assertEqual(484, result)


if __name__ == '__main__':
    unittest.main()
