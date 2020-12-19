f = open("../inputs/day19.txt", "r")

raw_rules, messages = f.read().split("\n\n")

rules = {}
for rule in raw_rules.split("\n"):
    rules[int(rule[:rule.index(":")])] = rule[rule.index(":")+2:]

messages = messages.split("\n")

matches = [set() for _ in range(len(rules))]


def pair(i, j):
    temp = set()
    for matchI in all_matches(i):
        for matchJ in all_matches(j):
            temp.add(matchI + matchJ)
    return temp


def get(parts):
    if len(parts) == 1:
        return all_matches(parts[0])
    else:
        return pair(parts[0], parts[1])


def all_matches(i):
    if len(matches[i]) > 0:
        return matches[i]
    if rules[i] in ["\"a\"", "\"b\""]:
        matches[i].add(rules[i][1])
        return matches[i]
    if "|" in rules[i]:
        ruleA, ruleB = rules[i].split(" | ")
        partsA = list(map(int, ruleA.split()))
        partsB = list(map(int, ruleB.split()))
        matches[i] = get(partsA) | get(partsB)
        return matches[i]
    parts = list(map(int, rules[i].split()))
    matches[i] = get(parts)
    return matches[i]


all_matches(0)

print("p1:", sum(message in matches[0] for message in messages))


def star(message, k):
    if message in matches[k]:
        return True
    for i in range(1, len(message)):
        if message[:i] in matches[k] and star(message[i:], k):
            return True
    return False


count = 0
for message in messages:
    good = False
    for i in range(1, len(message)):
        left = message[:i]
        if star(left, 42):
            right = message[i:]
            a, b = right[:len(right)//2], right[len(right)//2:]
            if star(a, 42) and star(b, 31):
                good = True
                break
    count += good
print("p2:", count)
