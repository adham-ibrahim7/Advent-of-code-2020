def solve(map, right, down):
    count = 0
    pos = 0
    for i in range(0, len(map), down):
        if map[i][pos] == "#":
            count += 1
        pos = (pos + right) % len(map[i])
    return count


if __name__ == "__main__":
    with open("../inputs/day3.txt", "r") as f:
        map = list(line[:-1] for line in f)

        ans = 1
        for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
            ans *= solve(map, r, d)

        print(ans)
