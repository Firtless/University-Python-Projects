import math


def max_length(w, heights):
    n = len(heights)
    count = 0
    if n < 2:
        return 0.0

    low_prev = 0.0
    high_prev = 0.0

    for i in range(1, n):
        low_low = low_prev + math.sqrt(w**2 + (1 - 1)**2)
        high_low = high_prev + math.sqrt(w**2 + (heights[i-1] - 1)**2)
        current_low = max(low_low, high_low)

        low_high = low_prev + math.sqrt(w**2 + (heights[i] - 1)**2)
        high_high = high_prev + \
            math.sqrt(w**2 + (heights[i] - heights[i-1])**2)
        current_high = max(low_high, high_high)

        low_prev = current_low
        high_prev = current_high
        count += 1

    res = max(low_prev, high_prev)
    print(f"{count}")
    return round(res + 1e-9, 2)
