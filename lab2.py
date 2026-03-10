import math


def min_board_space(n, w, h):
    board_side = max(math.isqrt(n * w * h), max(w, h))

    steps = 0

    while True:
        steps += 1
        count = (board_side // w) * (board_side // h)

        if count >= n:
            if ((board_side - 1) // w) * ((board_side - 1) // h) < n:
                break
            board_side -= 1
        else:
            perfect_ratio = math.sqrt(n // max(count, 1))
            board_side = max(board_side + 1, int(board_side * perfect_ratio))

    print(f'the amount of steps: {steps}')
    return board_side
