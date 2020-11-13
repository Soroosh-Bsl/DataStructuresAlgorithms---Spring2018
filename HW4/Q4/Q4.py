def modulo(a, b, n):
    r = 1
    while b > 0:
        if b & 1 == 1:
            r = r * a % n
        b //= 2
        a = a * a % n
    return r


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


n, m = map(int, input().split())
dsu = DisjointSet(n)
for i in range(m):
    u, v = map(int, input().split())
    dsu.union(dsu.nodes[u-1], dsu.nodes[v-1])
    print(modulo(2, dsu.dors, 10**9+9)-1)
