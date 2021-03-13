from collections import deque

N, M = map(int, input().split())
indegree = [0] * N
adj_lst = [[] for _ in range(N)]
answer = []

for _ in range(M):
    a, b = map(int, input().split())
    adj_lst[a-1].append(b-1)
    indegree[b-1] += 1

queue = deque()
for i in range(N):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    answer.append(x+1)
    for i in range(len(adj_lst[x])):
        dest = adj_lst[x][i]
        indegree[dest] -= 1
        if indegree[dest] == 0:
            queue.append(dest)

print(*answer)
