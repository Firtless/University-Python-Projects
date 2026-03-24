class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1


class AVLPriorityQueue:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, value, priority):
        self.root = self._insert_recursive(self.root, value, priority)

    def _insert_recursive(self, node, value, priority):
        if not node:
            return Node(value, priority)

        if priority >= node.priority:
            node.left = self._insert_recursive(node.left, value, priority)
        else:
            node.right = self._insert_recursive(node.right, value, priority)

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and priority >= node.left.priority:
            return self.rotate_right(node)
        if balance < -1 and priority < node.right.priority:
            return self.rotate_left(node)
        if balance > 1 and priority < node.left.priority:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and priority >= node.right.priority:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def peek(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return (current.value, current.priority)

    def pop(self):
        if not self.root:
            return None
        highest_info = self.peek()
        self.root = self._delete_recursive(self.root, highest_info[1])
        return highest_info

    def _delete_recursive(self, node, priority):
        if not node:
            return node

        if priority > node.priority:
            node.left = self._delete_recursive(node.left, priority)
        elif priority < node.priority:
            node.right = self._delete_recursive(node.right, priority)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self._get_min(node.right)
            node.priority = temp.priority
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.priority)

        if not node:
            return node

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def _get_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current
