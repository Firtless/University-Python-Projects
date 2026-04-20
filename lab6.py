import sys


def beer_problem(n, b, preferences):
    employees_likes = []
    prefs = preferences.split()

    for i in range(n):
        likes = set()
        for beer_index in range(b):
            if prefs[i][beer_index] == 'Y':
                likes.add(beer_index)
        employees_likes.append(likes)

    def min_beers(employee_idx, selected_beers):
        if employee_idx == n:
            return len(selected_beers)

        if any(beer in selected_beers for beer in employees_likes[employee_idx]):
            return min_beers(employee_idx + 1, selected_beers)

        min_count = float('inf')

        for beer in employees_likes[employee_idx]:
            selected_beers.add(beer)
            count = min_beers(employee_idx + 1, selected_beers)
            min_count = min(min_count, count)
            selected_beers.remove(beer)

        return min_count

    return min_beers(0, set())


if __name__ == "__main__":

    input_data = sys.stdin.read().split()
    if input_data:
        n_val = int(input_data[0])
        b_val = int(input_data[1])
        prefs_val = " ".join(input_data[2:])
        print(beer_problem(n_val, b_val, prefs_val))
