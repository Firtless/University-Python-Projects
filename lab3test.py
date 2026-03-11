import unittest
from lab3 import BinaryTree, tree_balanced


class TestBinaryTree(unittest.TestCase):

    def test_balanced_example(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        self.assertTrue(tree_balanced(root))

    # Tree from the task description
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5


def test_unbalanced_example(self):
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(3)
    self.assertFalse(tree_balanced(root))
    # Heavily left-leaning tree
    #       1
    #      /
    #     2
    #    /
    #   3


def test_empty_tree(self):
    self.assertTrue(tree_balanced(None))


def test_single_node(self):
    root = BinaryTree(10)
    self.assertTrue(tree_balanced(root))


def test_complex_unbalanced(self):
    root = BinaryTree(1)
    root.right = BinaryTree(2)
    root.left = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.left.left = BinaryTree(5)
    self.assertFalse(tree_balanced(root))


if __name__ == "__name__":
    unittest.main()
