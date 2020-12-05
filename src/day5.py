def convert(boarding_pass, lo, hi):
    if hi - lo == 1:
        return lo

    mid = (lo + hi) // 2
    if boarding_pass[0] in "FL":
        return convert(boarding_pass[1:], lo, mid)
    else:
        return convert(boarding_pass[1:], mid, hi)

if __name__ == "__main__":
    with open("../inputs/day5.txt", "r") as f:
        seats = []

        for line in f.read().split("\n"):
            row = convert(line[0:7], 0, 128)
            col = convert(line[7:], 0, 8)

            seats.append(8 * row + col)

        seats.sort()

        for i in range(len(seats)-1):
            if seats[i+1] - seats[i] != 1:
                print(seats[i]+1)