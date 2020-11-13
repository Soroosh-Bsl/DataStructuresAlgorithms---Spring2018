def BFS(graph, root):
    global maximumRank
    global n
    visited = [False] * n
    ranks = [0] * n
    queue = list()
    visited[root] = True
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        for neighbour in graph[node]:
            if not visited[neighbour]:
                ranks[neighbour] = ranks[node] + 1
                queue.append(neighbour)
                visited[neighbour] = True
    return max(ranks)

maximumRank = 0
n, m = map(int, input().split())
graph = [[] for i in range(n)]

for i in range(m):
    first, second = map(int, input().split())
    first, second = first - 1, second - 1
    graph[first].append(second)
    graph[second].append(first)

for i in range(n):
    newMax = BFS(graph, i)
    if newMax > maximumRank:
        maximumRank = newMax

print(maximumRank)
