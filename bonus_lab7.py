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


def spinner(duration):
    symbols = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f'\rScanning environment... {symbols[i % 4]}')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write('\rScanning complete!          \n')


def run_simulation(file_path, random_wells_count=2):
    os.system('clear' if os.name == 'posix' else 'cls')
    print("=== IoT TELECOM: INFRASTRUCTURE OPTIMIZER ===")
    spinner(1.5)

    edges = []
    nodes = set()

    # 1. Load existing data
    try:
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 3:
                    u, v, w = [item.strip() for item in row]
                    edges.append((int(w), u, v))
                    nodes.update([u, v])
    except FileNotFoundError:
        print(
            f"Warning: {file_path} not found. Starting with random data only.")

    # 2. Inject Random Wells
    for i in range(random_wells_count):
        new_well = f"RND-{random.randint(10, 99)}"
        if list(nodes):
            existing_well = random.choice(list(nodes))
            dist = random.randint(500, 3000)
            edges.append((dist, existing_well, new_well))
            nodes.add(new_well)
        else:
            nodes.add(new_well)

    if not nodes:
        print("Error: No data available.")
        return

    # 3. Simple Grid Visualization
    print("\n--- GEOGRAPHICAL WELL MAP ---")
    node_list = sorted(list(nodes))
    grid_size = 5
    for r in range(grid_size):
        line = "  "
        for c in range(grid_size):
            if (r * grid_size + c) < len(node_list):
                line += f"[{node_list[r * grid_size + c]}]   "
            else:
                line += ".       "
        print(line)
    time.sleep(1)

    # 4. Kruskal's Logic
    edges.sort()
    parent = {node: node for node in nodes}
    total_length = 0
    count = 0

    print("\n--- BUILDING OPTIMAL NETWORK ---")
    for weight, u, v in edges:
        sys.stdout.write(f"Link: {u} <-> {v} ({weight}m) ")
        time.sleep(0.4)

        if union(parent, u, v):
            total_length += weight
            count += 1
            print(">> [CONNECTED]")
        else:
            print(">> [REDUNDANT]")

    print("\n--- FINAL REPORT ---")
    if count == len(nodes) - 1:
        print(f"Integrity: SECURE")
        print(f"Total Cable: {total_length}m")
    else:
        print(f"Integrity: FAILED (-1)")
    print("============================================\n")


if __name__ == "__main__":
    # You can change '2' to any number of random wells you want
    run_simulation('communication_wells.csv', random_wells_count=2)
