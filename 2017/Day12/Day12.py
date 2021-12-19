infile = open("Day12.txt", "r")

def reachable(graph, start):
    q = [start]
    visited = set()
    while len(q) > 0:
        cur = q.pop(0)
        for i in graph[cur]:
            if i not in visited:
                visited.add(i)
                q.append(i)
    return visited

lines = infile.readlines()
graph = {}
for line in lines:
    l = line.rstrip().split(" <-> ")
    graph[l[0]] = l[1].split(", ")
ingroups = set()
numGroups = 0
for i in graph:
    if i not in ingroups:
        numGroups += 1
        ingroups = ingroups.union(reachable(graph, i))
print(numGroups)