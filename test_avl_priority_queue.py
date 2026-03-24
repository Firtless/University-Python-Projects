import unittest
import random
from avl_priority_queue import AVLPriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = AVLPriorityQueue()

    def test_logic(self):
        self.pq.insert("Low", 10)
        self.pq.insert("High", 100)
        self.pq.insert("Mid", 50)

        val, prio = self.pq.peek()
        self.assertEqual(prio, 100)

        self.assertEqual(self.pq.pop()[1], 100)
        self.assertEqual(self.pq.pop()[1], 50)
        self.assertEqual(self.pq.pop()[1], 10)

    def test_empty_behavior(self):
        self.assertIsNone(self.pq.peek())
        self.assertIsNone(self.pq.pop())

    def test_stress_and_balance(self):
        priorities = list(range(1, 101))
        random.shuffle(priorities)


if __name__ == "__main__":
    unittest.main()
