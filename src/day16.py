f = open("../inputs/day16.txt", "r")

fields, my_ticket, other_tickets = f.read().split("\n\n")

fields = fields.split("\n")
fieldnames = [field.split(": ")[0] for field in fields]
ranges = []

valid = set()

discarded = set()

for field in fields:
    range1, range2 = field.split(": ")[1].split(" or ")
    range1 = list(map(int, range1.split("-")))
    range2 = list(map(int, range2.split("-")))

    ranges.append(set(range(range1[0], range1[1]+1)) | set(range(range2[0], range2[1]+1)))

    valid |= ranges[-1]

other_tickets = [list(map(int, x.split(","))) for x in other_tickets.split("\n")[1:]]

ans1 = 0

for (i, ticket) in enumerate(other_tickets):
    for field in ticket:
        if field not in valid:
            ans1 += field
            discarded.add(i)

print("p1:", ans1)

possible = list([] for _ in range(len(fields)))

for i in range(len(fields)):
    for j in range(len(fields)):
        good = True
        for k, ticket in enumerate(other_tickets):
            if k in discarded:
                continue
            if ticket[j] not in ranges[i]:
                good = False
                break
        if good:
            possible[j].append(i)

configuration = [0] * len(fields)

placed = set()

for _ in range(len(fields)):
    for i in range(len(fields)):
        temp = []
        for p in possible[i]:
            if p not in placed:
                temp.append(p)
        possible[i] = temp
        if len(possible[i]) == 1:
            configuration[i] = possible[i][0]
            placed.add(configuration[i])

ans2 = 1
for i, value in enumerate(map(int, my_ticket.split("\n")[1].split(","))):
    if configuration[i] < 6:
        ans2 *= value

print("p2:", ans2)
