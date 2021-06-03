from collections import deque

queue = deque()

N = 5
node = [[1, 3], [3, 4], [2, 5]]
total = []

adj_lst = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for x, y in node:
    adj_lst[x].append(y)
print(adj_lst)

for i in range(1, N+1):
    if not visited[i]:
        area = 1
        visited[i] = 1
        queue.append(i)

    while queue:
        print(visited)
        x = queue.popleft()
        for y in adj_lst[x]:
            if not visited[y]:
                visited[y] = 1
                area += 1
                queue.append(y)
    total.append(area)

print(total)