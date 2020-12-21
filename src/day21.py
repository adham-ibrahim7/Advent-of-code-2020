f = open("../inputs/day21.txt", "r")

lines = f.read().split("\n")
lines = [line[:-1].split(" (contains ") for line in lines]

lines = [(line[0].split(), line[1].split(", ")) for line in lines]

possible = {}

for ingredients, allergens in lines:
    for allergen in allergens:
        if allergen not in possible:
            possible[allergen] = set(ingredients)
        else:
            possible[allergen] &= set(ingredients)

all_possible = set()
for allergen in possible:
    all_possible |= possible[allergen]

count = 0
for ingredients, _ in lines:
    for ingredient in ingredients:
        count += ingredient not in all_possible

print("p1:", count)

matching = {}
done = set()
while len(matching) < len(possible):
    for allergen in possible:
        remaining = []
        for ingredient in possible[allergen]:
            if ingredient not in done:
                remaining.append(ingredient)
        if len(remaining) == 1:
            ingredient = remaining[0]
            matching[ingredient] = allergen
            done.add(ingredient)

print("p2:", ",".join(sorted(matching, key=lambda a: matching[a])))


