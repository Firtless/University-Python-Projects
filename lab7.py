import csv


def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_x] = root_y
        return True
    return False


def min_cable(file_path):
    edges = []
    nodes = set()

    try:
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 3:
                    u, v, w = [item.strip() for item in row]
                    edges.append((int(w), u, v))
                    nodes.update([u, v])
    except FileNotFoundError:
        return -1

    if not nodes:
        return 0

    edges.sort()
    parent = {node: node for node in nodes}
    total_length = 0
    count = 0

    for weight, u, v in edges:
        if union(parent, u, v):
            total_length += weight
            count += 1

    return total_length if count == len(nodes) - 1 else -1
