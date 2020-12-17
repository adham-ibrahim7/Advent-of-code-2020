def neighbors3d(coord):
    x, y, z = coord
    neigh = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if dx == dy == dz == 0:
                    continue
                neigh.append((x + dx, y + dy, z + dz))
    return neigh


def neighbors4d(coord):
    x, y, z, w = coord
    neigh = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if dx == dy == dz == dw == 0:
                        continue
                    neigh.append((x + dx, y + dy, z + dz, w + dw))
    return neigh


def solve(p, neighbor_function):
    active = set()
    inactive = set()

    with open("../inputs/day17.txt", "r") as f:
        for x, line in enumerate(f.read().split("\n")):
            for y, c in enumerate(line):
                if c == ".":
                    continue
                coord = (x, y, 0) if p == 1 else (x, y, 0, 0)
                active.add(coord)
                for neigh in neighbor_function(coord):
                    inactive.add(neigh)

    for i in range(6):
        temp_active = set()
        temp_inactive = set()

        for coord in inactive:
            active_neighbors = sum(n in active for n in neighbor_function(coord))
            if active_neighbors == 3:
                temp_active.add(coord)

        for coord in active:
            active_neighbors = sum(n in active for n in neighbor_function(coord))
            if 2 <= active_neighbors <= 3:
                temp_active.add(coord)

        for coord in temp_active:
            for neigh in neighbor_function(coord):
                temp_inactive.add(neigh)

        active = temp_active
        inactive = temp_inactive

    print("p1:" if p == 1 else "p2:", len(active))


solve(1, neighbors3d)
solve(2, neighbors4d)
