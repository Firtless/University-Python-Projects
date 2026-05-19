import unittest
from lab9 import kmp_search


class TestKmpSearch(unittest.TestCase):

    def test_multiple_occurrences(self):
        self.assertEqual(kmp_search("ababcababab", "abab"), [0, 5, 7])

    def test_single_occurrence(self):
        self.assertEqual(kmp_search("hello politech", "politech"), [6])

    def test_no_occurrence(self):
        self.assertEqual(kmp_search("abcdefg", "xyz"), [])

    def test_overlapping_matches(self):
        self.assertEqual(kmp_search("aaaaa", "aaa"), [0, 1, 2])

    def test_empty_needle(self):
        self.assertEqual(kmp_search("anything", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(kmp_search("", "needle"), [])


if __name__ == "__main__":
    unittest.main()
