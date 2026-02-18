import unittest

from array_check import check_arr


class TestCheckArr(unittest.TestCase):
    def test_example_1(self):
        self.assertTrue(check_arr([1, 2, 3, 4, 5]))

    def test_example_2(self):
        self.assertTrue(check_arr([5, 4, 3, 2, 1]))

    def test_example_3(self):
        self.assertFalse(check_arr([1, 2, 2, 3, 2, 4, 5]))


if __name__ == '__main__':
    unittest.main()
