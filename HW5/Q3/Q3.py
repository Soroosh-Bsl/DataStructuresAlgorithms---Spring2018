def count_zir_derakht(graph, root, visited):
    global zoj
    global fard
    visited[root] = True
    numOfThisNode = 0
    for neighbour in graph[root]:
        if not visited[neighbour]:
            temp = count_zir_derakht(graph, neighbour, visited)
            numOfThisNode += temp + 1
    if numOfThisNode % 2 == 0:
        zoj += 1
    else:
        fard += 1
    # print(root+1, numOfThisNode)
    return numOfThisNode
zoj = 0
fard = 0

n = int(input())
graph = [[] for i in range(n)]
visited = [False] * n
for i in range(n-1):
    first, second = map(int, input().split())
    first, second = first - 1, second - 1
    graph[first].append(second)
    graph[second].append(first)

count_zir_derakht(graph, 0, visited)
print(zoj, fard)