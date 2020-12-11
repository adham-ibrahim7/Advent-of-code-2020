from copy import deepcopy

f = open("../inputs/day11.txt", "r")

orig = list(list(c for c in line) for line in f.read().split("\n"))


def update1(grid, i, j):
    occupied = 0
    for k in range(i-1, i+2):
        for h in range(j-1, j+2):
            if k == i and h == j or k < 0 or h < 0 or k >= len(grid) or h >= len(grid[0]):
                continue
            occupied += grid[k][h] == "#"
    if grid[i][j] == "L" and occupied == 0:
        return "#"
    elif grid[i][j] == "#" and occupied >= 4:
        return "L"
    else:
        return grid[i][j]


def iterate(grid, update_function):
    changes = 0

    copy = []

    for i in range(len(grid)):
        copy.append([])
        for j in range(len(grid[0])):
            copy[i].append(update_function(grid, i, j))
            changes += grid[i][j] != copy[i][j]

    return copy, changes


def update2(grid, i, j):
    occupied = 0
    for a in range(-1, 2):
        for b in range(-1, 2):
            if a == 0 and b == 0:
                continue
            ti, tj = i, j
            while 0 <= ti + a < len(grid) and 0 <= tj + b < len(grid[0]):
                ti += a
                tj += b
                if grid[ti][tj] != ".":
                    break
            if ti != i or tj != j:
                occupied += grid[ti][tj] == "#"
    if grid[i][j] == "L" and occupied == 0:
        return "#"
    elif grid[i][j] == "#" and occupied >= 5:
        return "L"
    else:
        return grid[i][j]


def solve(update_function, label):
    grid = deepcopy(orig)
    grid, changes = iterate(grid, update1)
    while changes > 0:
        grid, changes = iterate(grid, update_function)
    print(label, sum(grid[i][j] == "#" for i in range(len(grid)) for j in range(len(grid[0]))))


solve(update1, "p1:")
solve(update2, "p2:")
