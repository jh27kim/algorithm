from collections import defaultdict
import sys

sys.setrecursionlimit(100000)
UNVISITED = -1
answer = []


class Graph:
    global UNVISITED
    global answer

    def __init__(self, vertices):
        self.v = vertices
        self.g = defaultdict(list)
        self.id = 0

    def addEdge(self, u, v):
        self.g[u].append(v)

    def findSCCs(self):
        ids = [UNVISITED] * self.v
        low = [UNVISITED] * self.v

        onStack = [False] * self.v
        stack = []

        for i in range(self.v):
            if ids[i] == UNVISITED:
                self.dfs(i, low, ids, onStack, stack)

        return low

    def dfs(self, at, low, ids, onStack, stack):
        ids[at] = self.id
        low[at] = self.id
        self.id += 1

        onStack[at] = True
        stack.append(at)

        for to in self.g[at]:
            if ids[to] == UNVISITED:
                self.dfs(to, low, ids, onStack, stack)
                low[at] = min(low[at], low[to])

            elif onStack[to]:
                low[at] = min(low[at], ids[to])

        w = UNVISITED
        if low[at] == ids[at]:
            temp = []
            while w != at:
                w = stack.pop()
                temp.append(w+1)
                onStack[w] = False
                #low[w] = ids[at]
            answer.append(temp)


V, E = map(int, input().split())
g = Graph(V)
for _ in range(E):
    a, b = map(int, input().split())
    g.addEdge(a-1, b-1)
g.findSCCs()

for i in range(len(answer)):
    answer[i].sort()
answer.sort(key=lambda x: x[0])

print(len(answer))
for l in range(len(answer)):
    for i in answer[l]:
        print(i, end=" ")
    print('-1')
