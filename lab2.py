def min_board_space(n, w, h):
    min_num = min(w, h)
    max_num = max(w, h) * n

    result = max_num

    steps = 0

    while min_num <= max_num:

        steps += 1

        avr = (min_num + max_num) // 2
        count = (avr // w) * (avr // h)

        if count >= n:
            result = avr
            max_num = avr - 1
        else:
            min_num = avr + 1

    print(f'the amount of steps: {steps}')

    return result


# min1 = min_board_space(10000, 2, 3)
# print(min1)
