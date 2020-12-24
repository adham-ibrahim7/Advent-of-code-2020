line = open("../inputs/day23.txt", "r").read()
label = list(int(c) for c in line)


def solve(label, k):
    MAX = len(label)

    for _ in range(k):
        picked_up = label[1: 4]
        label = label[:1] + label[4:]

        destination = label[0] - 1
        if destination == 0:
            destination = MAX
        while destination in picked_up:
            destination -= 1
            if destination == 0:
                destination = MAX

        i = label.index(destination)
        label = label[0:i+1] + picked_up + label[i+1:]
        label = label[1:] + [label[0]]

        #i = label.index(1)
        #print(label[i:] + label[0:i])

    i = label.index(1)
    label = label[i+1:] + label[0:i]
    return label


print("p1:", "".join(map(str, solve(label, 100))))

label += list(range(10, 1_000_000))

solve(label, 200)