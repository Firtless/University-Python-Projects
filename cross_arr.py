arr_A = [1, 2, 4, 5]

arr_B = [2, 4, 6, 7]

cross = []


def task1(cross):
    for item in arr_A:
        if item in arr_B:
            cross.append(item)


task1(cross)

print(f"common items: {cross}")
