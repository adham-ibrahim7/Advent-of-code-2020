from functools import reduce

if __name__ == "__main__":
    with open("../inputs/day6.txt", "r") as f:
        all_lines = f.read().split("\n\n")

        print(sum(len(set(s for s in group if s != "\n")) for group in all_lines))
        print(sum(len(reduce(lambda x, y: x & y, (set(s for s in person) for person in group.split("\n")))) for group in all_lines))
