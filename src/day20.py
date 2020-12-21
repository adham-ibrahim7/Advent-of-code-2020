f = open("../inputs/day20.txt", "r")

tiles = f.read().split("\n\n")

tiles = [tile.split("\n") for tile in tiles]

ids = []
for i in range(len(tiles)):
    ids.append(int(tiles[i][0][5:9]))
    tiles[i] = tiles[i][1:]


def top(tile):
    return tile[0]


def bottom(tile):
    return tile[-1][::-1]


def right(tile):
    return "".join(tile[i][-1] for i in range(0, len(tile)))


def left(tile):
    return "".join(tile[i][0] for i in reversed(range(0, len(tile))))


adj = []

ans1 = 1
start = -1
for i in range(len(tiles)):
    possible = []
    for j in range(len(tiles)):
        if i == j:
            continue
        sides = [top, right, bottom, left]
        for x in range(4):
            for y in range(4):
                a, b = sides[x](tiles[i]), sides[y](tiles[j])
                if a == b or a == b[::-1]:
                    possible.append((j, x, y))
    adj.append(possible)
    if len(possible) == 2:
        ans1 *= ids[i]
        if start == -1:
            start = i

print("p1:", ans1)


def rotate(m):
    m = [[char for char in line] for line in m]
    return ["".join(row) for row in [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1, -1, -1)]]


def flip_hor(m):
    return [line[::-1] for line in m]


def flip_vert(m):
    return m[::-1]


def rotateK(m, k):
    return rotateK(rotate(m), k-1) if k > 0 else m


size = 12
image = list([-1] * size for _ in range(size))

remaining_tiles = set(range(len(tiles)))


def get_orientation(prev, i, j):
    prev_side = right if j > 0 else bottom
    curr_side = left if j > 0 else top
    flip = flip_hor if j > 0 else flip_vert

    for curr in remaining_tiles:
        for k in range(4):
            m = rotateK(tiles[curr], k)
            if curr_side(m) == prev_side(prev)[::-1]:
                return curr, k, None
            elif prev_side(m) == prev_side(prev):
                return curr, k, flip
    print("NONONO")


prev = start
for i in range(size):
    for j in range(size):
        if i + j == 0:
            image[i][j] = rotateK(tiles[start], 2)
            remaining_tiles.remove(start)
        else:
            prev = image[i][j-1] if j > 0 else image[i-1][j]
            curr, k, flip = get_orientation(prev, i, j)

            image[i][j] = rotateK(tiles[curr], k)
            if flip:
                image[i][j] = flip(image[i][j])
            remaining_tiles.remove(curr)

reduced_image = []

for i in range(size):
    for k in range(1, 9):
        line = ""
        for j in range(size):
            line += image[i][j][k][1:9]
        reduced_image.append(line)

monster =  \
[
"                  # ",
"#    ##    ##    ###",
" #  #  #  #  #  #   ",
]


def match(i, j, img):
    for k in range(3):
        for h in range(20):
            if i + k >= len(img) or j + h >= len(img[0]):
                return False
            if monster[k][h] == "#" and img[i+k][j+h] != monster[k][h]:
                return False
    return True


def solve(img):
    total = 0
    count = 0
    for i in range(len(img)):
        for j in range(len(img[0])):
            total += img[i][j] == "#"
            count += match(i, j, img)
    if count == 0:
        return -1
    return total - count * 15


oriented = flip_hor(rotateK(reduced_image, 3))
print(solve(oriented))
