class Node(object):
    # par = None
    # rank = 0
    # label = 0
    def __init__(self, label):
        self.label = label
        self.par = self
        self.rank = 0


class DisjointSet(object):
    # dors = 0
    # n = 0
    # nodes = None
    def __init__(self, n):
        self.dors = 0
        self.n = n
        self.nodes = [Node(i) for i in range(n)]

    def find(dsu, u):
        if u != u.par:  # here we user path compression trick
            u.par = dsu.find(u.par)
        return u.par

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:  # u and v are in the same component
            self.dors += 1
            return False

        # making v the vertex with better rank
        if u.rank > v.rank:
            u, v = v, u

        # merging two components
        u.par = v

        # updating maximum depth as rank
        if u.rank == v.rank:
            v.rank += 1

        return True


def nothing(x):
    return x


n, q = map(int, input().split())
dsu = DisjointSet(n)

last_zarbat = []
for i in range(n):
    last_zarbat.append(i)

for i in range(q):
    command, x, y = map(nothing, input().split())
    x, y = int(x), int(y)

    if command == "normal":
        dsu.union(dsu.nodes[x-1], dsu.nodes[y-1])
    elif command == "zarbati":
        x, y = x-1, y-1
        j = x
        while j < y:
            if last_zarbat[j] == j:
                dsu.union(dsu.nodes[j], dsu.nodes[y])
                last_zarbat[j] = y
                next = j + 1
            else:
                next = last_zarbat[j]
                last_zarbat[j] = y if y > last_zarbat[j] else last_zarbat[j]
            j = next
    elif command == "ask":
        x, y = dsu.find(dsu.nodes[x-1]), dsu.find(dsu.nodes[y-1])
        if x == y:
            print("Branko")
        else:
            print("Schafer")