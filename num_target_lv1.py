import unittest


def num_sum(nums, target):
    for i in range(len(nums)):
        for a in range(i + 1, len(nums)):
            if nums[i] + nums[a] == target:
                return [i, a]

    return -1


class TestTwoSum(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(num_sum([2, 7, 11, 15], 9), [0, 1])

    def test_example_2(self):
        self.assertEqual(num_sum([3, 2, 4], 6), [1, 2])

    def test_example_3(self):
        self.assertEqual(num_sum([3, 3], 6), [0, 1])

    def test_no_solution(self):
        self.assertEqual(num_sum([3, 5], 6), -1)


if __name__ == '__main__':
    unittest.main()
