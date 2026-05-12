import unittest
from lab8 import max_length


class TestElectricianTask(unittest.TestCase):

    def test_example_max(self):
        w = 2
        heights = [3, 3, 3]
        result = max_length(w, heights)
        self.assertEqual(result, 5.66)

    def test_example_similiar(self):
        w = 100
        heights = [1, 1, 1, 1]
        result = max_length(w, heights)
        self.assertEqual(result, 300.0)

    def test_example_diff(self):
        w = 4
        heights = [100, 2, 100, 2, 100]
        result = max_length(w, heights)
        self.assertEqual(result, 396.32)

    def test_large_dataset(self):
        w = 4
        heights = [
            56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5, 91,
            25, 17, 88, 66, 28, 2, 95, 97, 60, 93, 40, 70, 75, 48, 38, 51, 34,
            52, 87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51, 11, 39, 72
        ]
        result = max_length(w, heights)
        self.assertEqual(result, 2738.18)

    def test_single_pole(self):
        w = 10
        heights = [50]
        result = max_length(w, heights)
        self.assertEqual(result, 0.0)


if __name__ == '__main__':
    unittest.main()
