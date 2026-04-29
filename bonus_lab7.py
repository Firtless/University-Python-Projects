import csv
import time
import os
import sys
import random


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


def run_spinner(duration):
    symbols = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(
            f'\rMapping Infrastructure Topology... {symbols[i % 4]}')
        sys.stdout.flush()
        time.sleep(0.3)
        i += 1
    sys.stdout.write('\rScan Complete!                      \n')


def run_simulation(file_path, random_wells_count=5):
    os.system('clear' if os.name == 'posix' else 'cls')
    print("=== IoT TELECOM: FULL-LABEL VISUALIZER ===")
    run_spinner(1.0)

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
        pass

    for _ in range(random_wells_count):
        new_well = f"RND-{random.randint(10, 99)}"
        if nodes:
            existing_well = random.choice(list(nodes))
            dist = random.randint(500, 3000)
            edges.append((dist, existing_well, new_well))
        nodes.add(new_well)

    if not nodes:
        return

    node_list = sorted(list(nodes))
    coords = {}

    for node in node_list:
        while True:
            x, y = random.randint(2, 70), random.randint(1, 18)
            if all(abs(x - cx) > 8 or abs(y - cy) > 1 for cx, cy in coords.values()):
                coords[node] = (x, y)
                break

    print("\n--- GEOGRAPHICAL NODE DEPLOYMENT (FULL LABELS) ---")
    canvas = [[" " for _ in range(82)] for _ in range(20)]

    for node, (x, y) in coords.items():
        canvas[y][x] = "O"
        for i, char in enumerate(node):
            if x + i + 1 < 81:
                canvas[y][x + i + 1] = char

    for row in canvas:
        print("".join(row))

    print("-" * 82)
    time.sleep(1.0)

    edges.sort()
    parent = {node: node for node in nodes}
    total_length, count = 0, 0

    print("\n--- KRUSKAL'S OPTIMAL ROUTING ---")
    for weight, u, v in edges:
        sys.stdout.write(f"Testing: {u:<7} <-> {v:<7} ({weight:>4}m) ")
        sys.stdout.flush()
        time.sleep(0.3)

        if union(parent, u, v):
            total_length += weight
            count += 1
            print(">> [DEPLOYED]")
        else:
            print(">> [REDUNDANT]")

    print("\n--- FINAL NETWORK STATUS ---")
    if count == len(nodes) - 1:
        print(f"Connectivity: SECURE | Total Cable: {total_length}m")
    else:
        print(f"Connectivity: PARTIAL (-1)")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    run_simulation('communication_wells.csv', random_wells_count=14)
