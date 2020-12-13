f = open("../inputs/day12.txt", "r")

instructions = f.read().split("\n")

x, y, angle = 0, 0, 0


def execute1(instruction):
    global x, y, angle

    if instruction[0] == "N":
        y += int(instruction[1:])
    elif instruction[0] == "E":
        x += int(instruction[1:])
    elif instruction[0] == "S":
        y -= int(instruction[1:])
    elif instruction[0] == "W":
        x -= int(instruction[1:])
    elif instruction[0] == "L":
        angle += int(instruction[1:])
    elif instruction[0] == "R":
        angle -= int(instruction[1:])
    else:
        angle %= 360
        execute1("ENWS"[angle // 90] + instruction[1:])


def execute2(instruction):
    global x, y, sx, sy

    if instruction[0] == "N":
        y += int(instruction[1:])
    elif instruction[0] == "E":
        x += int(instruction[1:])
    elif instruction[0] == "S":
        y -= int(instruction[1:])
    elif instruction[0] == "W":
        x -= int(instruction[1:])
    elif instruction[0] == "F":
        times = int(instruction[1:])
        sx += times * x
        sy += times * y
    else:
        angle = int(instruction[1:])
        if instruction[0] == "L":
            angle = 360 - angle
        while angle > 0:
            x, y = y, -x
            angle -= 90


for instruction in instructions:
    execute1(instruction)

print("p1:", abs(x) + abs(y))

x, y = 10, 1
sx, sy = 0, 0

for instruction in instructions:
    execute2(instruction)

print("p2:", abs(sx) + abs(sy))