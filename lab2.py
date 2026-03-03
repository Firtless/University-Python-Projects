def min_board_space(n, w, h):
    min_num = 1
    max_num = max(w, h) * n
    result = max_num

    while min_num <= max_num:
        avr = (min_num + max_num) // 2
        count = (avr // w) * (avr // h)

        if count >= n:
            result = avr
            max_num = avr - 1
        else:
            min_num = avr + 1

    return result
