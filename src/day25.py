f = open("../inputs/day25.txt", "r")

c, d = map(int, f.readlines())

MOD = 20201227


def determine_pow(remainder):
    a = 0
    n = 1
    while n != c:
        a += 1
        n = n * 7 % MOD
    return a


a, b = determine_pow(c), determine_pow(d)


def modpow(a, b, m):
    if b == 0:
        return 1
    res = modpow(a, b // 2, m)
    res *= res
    if b % 2 == 1:
        res *= a
    return res % m


print("p1:", modpow(d, b, MOD))
