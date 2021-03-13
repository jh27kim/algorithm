from collections import deque
from math import log2

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, c = map(int, input().split())
    tree[c].append(p)
    tree[p].append(c)

parents = [0] * (N+1)
depth = [0] * (N+1)
check = [True] * (N+1)

q = deque()
q.append(1)

while q:
    x = q.popleft()
    check[x] = False
    for node in tree[x]:
        if check[node]:
            q.append(node)
            parents[node] = x
            depth[node] = depth[x] + 1

logN = int(log2(N)) + 1
DP = [[0 for _ in range(logN)] for i in range(N+1)]

for i in range(N+1):
    DP[i][0] = parents[i]

for j in range(1, int(log2(N))+1):
    for i in range(1, N+1):
        if DP[i][j-1] != 0:
            DP[i][j] = DP[DP[i][j-1]][j-1]


M = int(input())
for _ in range(M):
    a, b = map(int, input().split())

    if depth[a] > depth[b]:
        a, b = b, a

    diff = depth[b] - depth[a]
    for i in range(logN-1, -1, -1):
        if diff >= 1 << i:
            diff -= 1 << i
            b = DP[b][i]

    if a == b:
        print(a)
        continue

    for i in range(logN-1, -1, -1):
        if DP[a][i] != DP[b][i]:
            a = DP[a][i]
            b = DP[b][i]

    print(DP[b][0])

