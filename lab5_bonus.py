import collections


def find_warehouse_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = collections.deque([(start[0], start[1], 0)])
    visited = {start}

    while queue:
        r, c, dist = queue.popleft()

        if (r, c) == end:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return -1


warehouse_map = [
    [0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0]
]

start_point = (0, 0)
end_point = (5, 5)

if __name__ == "__main__":
    steps = find_warehouse_path(warehouse_map, start_point, end_point)

    if steps != -1:
        print(f"Result: {steps} steps.")
    else:
        print("No path found.")
