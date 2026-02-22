arr_A = [1, 2, 4, 5, 9, 0]

arr_B = [2, 4, 6, 7, 8]

cross = []
multi_result = []


def task1(cross):
    for item in arr_A:
        if item in arr_B:
            cross.append(item)


task1(cross)


def task2(multi_result):
    for a in arr_A:
        for b in arr_B:
            result = a * b
            multi_result.append(result)


task2(multi_result)


print(
    f"common items: {cross} and cartesian product of two arrays: {multi_result}")
