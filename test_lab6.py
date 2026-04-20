import unittest
from lab6 import beer_problem


class TestBeerProblem(unittest.TestCase):

    def test_example_1(self):
        n, b = 2, 2
        prefs = "YN NY"
        result = beer_problem(n, b, prefs)
        self.assertEqual(result, 2)

    def test_example_2(self):
        n, b = 6, 3
        prefs = "YNN YNY YNY NYY NYY NYN"
        result = beer_problem(n, b, prefs)
        self.assertEqual(result, 2)

    def test_all(self):
        n, b = 3, 2
        prefs = "YY YN NY"
        self.assertEqual(beer_problem(n, b, prefs), 2)

    def test_single(self):
        n, b = 2, 1
        prefs = "Y Y"
        self.assertEqual(beer_problem(n, b, prefs), 1)


if __name__ == '__main__':
    unittest.main()
