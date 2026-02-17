import unittest


def check_arr(arr):

    is_up = True
    is_down = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            is_up = False
        elif arr[i] < arr[i + 1]:
            is_down = False

    return is_up or is_down


class TestCheckArr(unittest.TestCase):
    def test_example_1(self):
        self.assertTrue(check_arr([1, 2, 3, 4, 5]))

    def test_example_2(self):
        self.assertTrue(check_arr([5, 4, 3, 2, 1]))

    def test_example_3(self):
        self.assertFalse(check_arr([1, 2, 2, 3, 2, 4, 5]))


if __name__ == '__main__':
    unittest.main()
