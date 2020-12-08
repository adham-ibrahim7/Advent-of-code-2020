f = open("../inputs/day7.txt", "r")

node_map = {}
current_label = 0

adj = [[] for _ in range(1000)]
rev_adj = [[] for _ in range(1000)]

for line in f.read().split("\n"):
    outer, inner_list = line.split(" contain ")

    outer = outer.split(" bag")[0]

    if outer not in node_map:
        node_map[outer] = current_label
        current_label += 1

    for inner in inner_list.split(", "):
        inner = inner.split(" bag")[0]

        if inner == "no other":
            continue

        count, inner = int(inner[0]), inner[2:]

        if inner not in node_map:
            node_map[inner] = current_label
            current_label += 1

        u, v = node_map[inner], node_map[outer]

        adj[u].append(v)
        rev_adj[v].append((u, count))

vis = [False] * len(node_map)


def dfs1(node):
    vis[node] = True
    for neigh in adj[node]:
        dfs1(neigh)


dfs1(node_map["shiny gold"])

print("p1:", sum(vis)-1)


def dfs2(node):
    total = 1
    for neigh, count in rev_adj[node]:
        total += count * dfs2(neigh)
    return total


print("p2:", dfs2(node_map["shiny gold"])-1)
