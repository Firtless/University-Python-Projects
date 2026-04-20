import random


def satellite_simulation():
    n_regions = 15
    s_available = 25
    map_data = []
    for _ in range(n_regions):
        row = ""
        for _ in range(s_available):
            row += "Y" if random.random() < 0.15 else "N"
        if "Y" not in row:
            pos = random.randint(0, s_available - 1)
            row = row[:pos] + "Y" + row[pos+1:]
        map_data.append(row)

    region_requirements = []
    for i in range(n_regions):
        coverage = set()
        for j in range(s_available):
            if map_data[i][j] == 'Y':
                coverage.add(j)
        region_requirements.append(coverage)

    def min_set(idx, current_set):
        if idx == n_regions:
            return list(current_set)

        if any(s in current_set for s in region_requirements[idx]):
            return min_set(idx + 1, current_set)

        best_result = None
        for s in region_requirements[idx]:
            current_set.add(s)
            res = min_set(idx + 1, current_set)
            if best_result is None or (res and len(res) < len(best_result)):
                best_result = list(res)
            current_set.remove(s)
        return best_result

    selected_ids = min_set(0, set())

    satellite_specs = {}
    for s_id in selected_ids:
        is_priority = random.random() < 0.3
        satellite_specs[s_id] = {
            "priority": is_priority,
            "radius": 4 if is_priority else 2
        }

    grid_size = 10
    grid = [['·' for _ in range(grid_size)] for _ in range(grid_size)]
    placements = {}
    failed_to_place = []
    sorted_ids = sorted(
        selected_ids, key=lambda x: satellite_specs[x]['priority'], reverse=True)

    for s_id in sorted_ids:
        spec = satellite_specs[s_id]
        placed = False
        attempts = 0
        while not placed and attempts < 1000:
            r = random.randint(0, grid_size - 1)
            c = random.randint(0, grid_size - 1)
            can_fit = True
            rad = spec["radius"]

            for dr in range(-rad, rad + 1):
                for dc in range(-rad, rad + 1):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < grid_size and 0 <= nc < grid_size:
                        if grid[nr][nc] != '·':
                            can_fit = False
                            break
                if not can_fit:
                    break

            if can_fit:
                grid[r][c] = 'P' if spec["priority"] else 'S'
                placements[s_id] = (r, c)
                placed = True
            attempts += 1

        if not placed:
            failed_to_place.append(s_id)

    print("\n" + "="*60)
    print("      MISSION CONTROL: GLOBAL SATELLITE OPTIMIZER")
    print("="*60)
    print(f"Regions Managed: {n_regions} | Orbits Scanned: {s_available}")
    print(f"Optimization Goal: Minimum coverage for 100% Signal")
    print(f"Minimum Satellites Required: {len(selected_ids)}")
    print("-" * 60)

    for s_id in selected_ids:
        spec = satellite_specs[s_id]
        status = "ONLINE" if s_id in placements else "BLOCKED"
        pos = placements.get(s_id, "COLLISION")
        type_str = "PRIORITY" if spec['priority'] else "STANDARD"
        print(f"NODE-{s_id:02} | {type_str:8} | Status: {status:7} | POS: {pos}")

    print("\n--- ORBITAL SECTOR VISUALIZATION ---")
    for row in grid:
        print(" ".join(row))
    print(
        "\nLEGEND: [P] Priority Node (Large Buffer) | [S] Standard Node | [·] Empty Orbit")


if __name__ == "__main__":
    satellite_simulation()
