def check_arr(arr):

    is_up = True
    is_down = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            is_up = False
        elif arr[i] < arr[i + 1]:
            is_down = False

    return is_up or is_down
