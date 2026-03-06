import math


def min_board_space(n, w, h):
    side = max(math.isqrt(n * w * h), max(w, h))

    steps = 0

    while True:
        steps += 1
        count = (side // w) * (side // h)

        if count >= n:
            if ((side - 1) // w) * ((side - 1) // h) < n:
                break
            side -= 1
        else:
            needed_ratio = math.sqrt(n // max(count, 1))
            side = max(side + 1, int(side * needed_ratio))

    print(f'the amount of steps: {steps}')
    return side
