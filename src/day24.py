import math

f = open("../inputs/day24.txt", "r")

lines = f.read().split("\n")


def convert(line):
    if len(line) == 0:
        return []
    if line[0] in "ew":
        return [line[0]] + convert(line[1:])
    else:
        return [line[0:2]] + convert(line[2:])


lines = [convert(line) for line in lines]

directions = ['e', 'ne', 'nw', 'w', 'sw', 'se']


def rounded(pos):
    return round(pos[0], 6), round(pos[1], 6)


black = set()
for line in lines:
    pos = (0, 0)
    for dir in line:
        rad = math.radians(60 * directions.index(dir))
        pos = (pos[0] + math.cos(rad), pos[1] + math.sin(rad))

    pos = rounded(pos)

    if pos in black:
        black.remove(pos)
    else:
        black.add(pos)

print("p1:", len(black))


def neighbors(pos):
    neighb = []
    for dir in range(0, 360, 60):
        rad = math.radians(dir)
        neigh = (pos[0] + math.cos(rad), pos[1] + math.sin(rad))
        neighb.append(neigh)
    return neighb


all_positions = set()
for x in range(-200, 200):
    for y in range(-200, 200):
        all_positions.add((x * 0.5, y * math.sqrt(3) * 0.5))

for i in range(100):
    print(i)
    temp_black = set()

    for pos in all_positions:
        count = sum(rounded(neigh) in black for neigh in neighbors(pos))
        if rounded(pos) in black:
            if 1 <= count <= 2:
                temp_black.add(rounded(pos))
        elif count == 2:
            temp_black.add(rounded(pos))

    black = temp_black

print("p2:", len(black))
