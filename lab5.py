import collections


def shortest_path(n, start, end):
    if start == end:
        return 0

    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [-1, 1, 1, -1, 2, -2, 2, -2]

    queue = collections.deque([(start[0], start[1], 0)])
    visited = {start}

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == end:
            return dist

        for i in range(8):
            nx, ny = x + row[i], y + col[i]

            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))

    return -1


def process_file():
    try:
        with open('input.txt', 'r') as f:
            lines = f.readlines()
            n = int(lines[0])
            start = tuple(map(int, lines[1].split(',')))
            end = tuple(map(int, lines[2].split(',')))

        result = shortest_path(n, start, end)

        with open('output.txt', 'w') as f:
            f.write(str(result))
    except FileNotFoundError:
        pass


def unsorted_range(arr):
    n = len(arr)
    if n < 2:
        return (-1, -1)

    left = 0
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1

    if left == n - 1:
        return (-1, -1)

    right = n - 1
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1

    sub_arr = arr[left:right + 1]
    sub_min = min(sub_arr)
    sub_max = max(sub_arr)

    while left > 0 and arr[left - 1] > sub_min:
        left -= 1
    while right < n - 1 and arr[right + 1] < sub_max:
        right += 1

    return (left, right)


if __name__ == "__main__":
    process_file()
