f = open("../inputs/day15.txt")

init = list(map(int, f.read().split(",")))


def solve(n):
    last = {}

    for i in range(0, n):
        if i < len(init):
            curr = init[i]
        else:
            curr = next

        if curr not in last:
            next = 0
        else:
            next = i - last[curr]

        last[curr] = i
    return curr

    # print(i, curr)


print("p1:", solve(2020))
print("p2:", solve(30000000))
