f = open("../inputs/day13.txt", "r")

min_depart = int(f.readline())

raw = f.readline().split(",")

best_time, id = 10000000, 0

for s in raw:
    if s == "x":
        continue
    bus = int(s)
    time = min_depart // bus * bus
    if time < min_depart:
        time += bus
    if time - min_depart < best_time:
        best_time = time - min_depart
        id = bus

print("p1:", best_time * id)


def bin_pow(a, b, m):
    if b == 0:
        return 1
    res = bin_pow(a, b // 2, m)
    res *= res
    if b % 2 == 1:
        res *= a
    return res % m


a, m = [], []
product = 1
for (i, s) in enumerate(raw):
    if s == "x":
        continue

    m.append(int(s))
    product *= m[-1]
    a.append((m[-1] - i) % m[-1])

X = list(product // mi for mi in m)


def inverse(x, m):
    return bin_pow(x, m - 2, product)


t = sum(a[i] * X[i] * inverse(X[i], m[i]) for i in range(len(a))) % product

print(t)
