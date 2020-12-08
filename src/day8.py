f = open("../inputs/day8.txt", "r")

instructions = [full_instruction.split(" ") for full_instruction in f.read().split("\n")]


def run(instructions):
    vis = [False] * len(instructions)

    acc = 0
    curr = 0

    terminated = False

    while not vis[curr]:
        vis[curr] = True
        name, value = instructions[curr]
        value = int(value)
        if name == "jmp":
            curr += value
        elif name == "acc":
            acc += value
            curr += 1
        else:
            curr += 1
        if curr >= len(vis):
            terminated = True
            break

    return acc, terminated


def flip(val):
    if val == "nop":
        return "jmp"
    elif val == "jmp":
        return "nop"
    return val


acc = run(instructions)[0]

print("p1:", acc)

for i in range(len(instructions)):
    instruction = instructions[i]
    instructions[i][0] = flip(instructions[i][0])
    acc, terminated = run(instructions)
    if terminated:
        print("p2:", acc)
        break
    instructions[i][0] = flip(instructions[i][0])
