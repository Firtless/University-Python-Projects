import math
import time
import random
import sys
from colorama import Fore, Style, init

init(autoreset=True)


def simulate_connection(w, heights):
    n = len(heights)
    if n < 2:
        return 0.0, []

    low_prev = 0.0
    high_prev = 0.0

    for i in range(1, n):
        low_low = low_prev + math.sqrt(w**2 + (1 - 1)**2)
        high_low = high_prev + math.sqrt(w**2 + (heights[i-1] - 1)**2)

        low_high = low_prev + math.sqrt(w**2 + (heights[i] - 1)**2)
        high_high = high_prev + \
            math.sqrt(w**2 + (heights[i] - heights[i-1])**2)

        if low_low > high_low:
            current_low = low_low
        else:
            current_low = high_low

        if low_high > high_high:
            current_high = low_high
        else:
            current_high = high_high

        low_prev = current_low
        high_prev = current_high

    final_res = max(low_prev, high_prev)
    return round(final_res + 1e-9, 2)


def rgb_banner(text, duration=3):
    start_time = time.time()
    while time.time() - start_time < duration:
        t = time.time()
        r = int(127 * math.sin(t * 3) + 128)
        g = int(127 * math.sin(t * 3 + 2) + 128)
        b = int(127 * math.sin(t * 3 + 4) + 128)

        sys.stdout.write(f"\r\033[38;2;{r};{g};{b}m--- {text} ---\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)
    print()


def spinner(duration):
    chars = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in chars:
            sys.stdout.write(f'\r{Fore.CYAN}Analyzing grid stability {char}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * 30 + '\r')


def render_preview(heights):
    print(f"{Fore.YELLOW}POLE CONFIGURATION PREVIEW:")
    max_h = max(heights)
    for level in range(5, 0, -1):
        row = ""
        threshold = (max_h / 5) * level
        for h in heights:
            if h >= threshold:
                row += f"{Fore.WHITE}  |  "
            else:
                row += "     "
        print(row)
    print(f"{Fore.GREEN}" + " === " * len(heights))


def export_savings(final_val, raw_total):
    savings = round(raw_total - final_val, 2)
    with open("resource_savings.txt", "a") as f:
        f.write(f"Session: {time.ctime()}\n")
        f.write(f"Optimized Length: {final_val}m\n")
        f.write(f"Estimated Material Saved: {max(0, savings)}m\n")
        f.write("-" * 30 + "\n")


def pole_demo():
    NUM_POLES = 12
    DISTANCE = 15

    rgb_banner("WIRE OPTIMIZATION SYSTEM", duration=4)

    generated_heights = [random.randint(10, 100) for _ in range(NUM_POLES)]
    render_preview(generated_heights)

    spinner(3)

    max_wire = simulate_connection(DISTANCE, generated_heights)
    theoretical_max = sum(generated_heights)

    print(f"\n{Fore.GREEN}[SUCCESS] Calculation Complete")
    print(f"{Fore.WHITE}Optimized Wire: {Fore.YELLOW}{max_wire} units")

    export_savings(max_wire, theoretical_max)
    print(f"{Fore.BLUE}Log file 'resource_savings.txt' updated.")


if __name__ == "__main__":
    pole_demo()
