import unittest
from lab5 import unsorted_range


class TestSubarrayLogic(unittest.TestCase):

    def test_sorted(self):
        self.assertEqual(unsorted_range([1, 2, 3, 4, 5]), (-1, -1))

    def test_unsorted(self):
        self.assertEqual(unsorted_range([5, 4, 3, 2, 1]), (0, 4))

    def test_single(self):
        self.assertEqual(unsorted_range([10]), (-1, -1))

    def test_example(self):
        arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        self.assertEqual(unsorted_range(arr), (3, 9))


if __name__ == '__main__':
    unittest.main()
