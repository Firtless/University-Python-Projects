import collections
import random


def get_path(n, start, end):
    if start == end:
        return [start]

    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [-1, 1, 1, -1, 2, -2, 2, -2]

    queue = collections.deque([(start[0], start[1], [start])])
    visited = {start}

    while queue:
        x, y, path = queue.popleft()
        if (x, y) == end:
            return path

        for i in range(8):
            nx, ny = x + row[i], y + col[i]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, path + [(nx, ny)]))
    return None


def simulate():
    n = 8
    names = ["White K1", "White K2", "Black K1", "Black K2"]

    knights = []
    for name in names:
        start = (random.randint(0, 7), random.randint(0, 7))
        goal = (0, 7) if "White" in name else (7, 0)
        path = get_path(n, start, goal)
        knights.append([name, start, goal, path, True, False])

    print("<<< SPAWN POINTS >>>")
    for k in knights:
        print(f"{k[0]}: Spawn {k[1]} -> Goal {k[2]}")

    max_len = max(len(k[3]) for k in knights if k[3])

    for step in range(1, max_len):
        positions = {}

        for k in knights:
            if not k[4] or k[5]:
                continue

            if step < len(k[3]):
                k[1] = k[3][step]
                curr_pos = k[1]

                if curr_pos in positions:
                    other_idx = positions[curr_pos]
                    print(
                        f"Collision at {curr_pos}: {k[0]} and {knights[other_idx][0]} removed")
                    k[4] = False
                    knights[other_idx][4] = False
                else:
                    positions[curr_pos] = knights.index(k)

                    if curr_pos == k[2]:
                        k[5] = True
                        k[4] = False
                        print(f"{k[0]} reached the goal!")

    print("\n<<< FINAL RESULTS >>>")
    for k in knights:
        res = "Winner" if k[5] else ("Crashed" if not k[4] else "Failed")
        print(f"{k[0]}: {res}")


if __name__ == "__main__":
    simulate()
