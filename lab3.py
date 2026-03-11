class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_hight(node):
    if node is None:
        return 0
    return 1 + max(tree_hight(node.left), tree_hight(node.right))


def tree_balanced(node: BinaryTree):
    if node is None:
        return True

    left_hight = tree_hight(node.left)
    right_hight = tree_hight(node.right)

    if abs(left_hight - right_hight) > 1:
        return False

    return tree_balanced(node.left) and tree_balanced(node.right)
