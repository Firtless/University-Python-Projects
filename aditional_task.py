import os


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def postorder_list(self, nodes):
        if self.left:
            self.left.postorder_list(nodes)
        if self.right:
            self.right.postorder_list(nodes)
        nodes.append(self.value)

    def find_successor(self, target_value):
        nodes = []
        self.postorder_list(nodes)
        for i in range(len(nodes) - 1):
            if nodes[i] == target_value:
                return nodes[i + 1]
        return None


def build_custom_tree(data_list):
    if not data_list:
        return None
    nodes = {int(''.join(filter(str.isdigit, item))): BinaryTree(int(''.join(filter(str.isdigit, item))))
             for item in data_list if any(c.isdigit() for c in item)}

    root_val = int(''.join(filter(str.isdigit, data_list[-1])))
    root = nodes[root_val]

    if 2 in nodes:
        root.left = nodes[2]
    if 4 in nodes:
        nodes[2].left = nodes[4]
    if 3 in nodes:
        nodes[2].right = nodes[3]
    if 5 in nodes:
        nodes[4].left = nodes[5]
    if 6 in nodes:
        nodes[4].right = nodes[6]
    if 11 in nodes:
        nodes[3].left = nodes[11]
    if 12 in nodes:
        nodes[11].right = nodes[12]
    if 13 in nodes:
        nodes[12].left = nodes[13]
    if 14 in nodes:
        nodes[13].right = nodes[14]
    if 15 in nodes:
        nodes[14].left = nodes[15]
    if 16 in nodes:
        nodes[14].right = nodes[16]
    if 7 in nodes:
        root.right = nodes[7]
    if 8 in nodes:
        nodes[7].right = nodes[8]
    if 9 in nodes:
        nodes[8].left = nodes[9]
    if 10 in nodes:
        nodes[8].right = nodes[10]
    if 17 in nodes:
        nodes[7].left = nodes[17]
    if 18 in nodes:
        nodes[17].right = nodes[18]
    if 19 in nodes:
        nodes[18].left = nodes[19]
    if 20 in nodes:
        nodes[18].right = nodes[20]

    return root


def render_to_grid(tree, mode="2d"):
    width, height = 120, 40
    grid = [[" " for _ in range(width)] for _ in range(height)]

    def write(x, y, text):
        if 0 <= y < height:
            s = str(text)
            for i, c in enumerate(s):
                if 0 <= x + i < width:
                    grid[y][x + i] = c

    if mode == "2d":
        def draw_2d(node, x, y, x_step):
            if not node:
                return
            write(x, y, node.value)
            if node.left:
                write(x - x_step//2, y + 1, "/")
                draw_2d(node.left, x - x_step, y + 2, max(2, x_step // 2))
            if node.right:
                write(x + x_step//2, y + 1, "\\")
                draw_2d(node.right, x + x_step, y + 2, max(2, x_step // 2))
        draw_2d(tree, 60, 1, 24)

    else:
        cx, cy = 60, 20
        write(cx, cy, tree.value)

        def draw_math_top(node, x, y, dx_sign, y_step):
            dx = 10 * dx_sign
            if node.left:
                nx, ny = x + dx, y + y_step
                char = "/" if dx_sign < 0 else "\\"
                write(x + dx//2, y + y_step//2, char)
                write(nx, ny, node.left.value)
                draw_math_top(node.left, nx, ny, dx_sign, max(2, y_step - 1))
            if node.right:
                nx, ny = x + dx, y - y_step
                char = "\\" if dx_sign < 0 else "/"
                write(x + dx//2, y - y_step//2, char)
                write(nx, ny, node.right.value)
                draw_math_top(node.right, nx, ny, dx_sign, max(2, y_step - 1))

        if tree.left:
            for i in range(cx - 6, cx):
                grid[cy][i] = "-"
            write(cx - 8, cy, tree.left.value)
            draw_math_top(tree.left, cx - 8, cy, -1, 6)

        if tree.right:
            for i in range(cx + 2, cx + 8):
                grid[cy][i] = "-"
            write(cx + 9, cy, tree.right.value)
            draw_math_top(tree.right, cx + 9, cy, 1, 6)

    for row in grid:
        line = "".join(row).rstrip()
        if line:
            print(line)


if __name__ == "__main__":
    file_path = "lab.txt"
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = f.read().split()
        tree = build_custom_tree(data)
        if tree:
            print("\n--- GENERATED 2D VIEW (20 NODES) ---")
            render_to_grid(tree, mode="2d")
            print("\n--- GENERATED TOP VIEW (20 NODES) ---")
            render_to_grid(tree, mode="top")
