import copy
from collections import deque


def solution(n, start, end, roads, traps):
    MAX = int(1e9)
    distance = [MAX] * (n + 1)
    distance[start] = 0
    visited = [[0 for _ in range(n+1)] for _ in range(n+1)]

    queue = deque()
    queue.append(start)

    adj_lst = [[] for _ in range(n+1)]
    adj_lst_inv = [[] for _ in range(n+1)]

    for a, b, cost in roads:
        adj_lst[a].append([b, cost])
        adj_lst_inv[b].append([a, cost])

    while queue:
        x = queue.popleft()
        print(x)

        if x in traps:
            temp_inv = copy.deepcopy(adj_lst_inv)
            temp = copy.deepcopy(adj_lst)

            for y, c in adj_lst_inv[x]:
                #Incoming Edges
                # x도착 y출발 edge 제거/y출발 x도착 추가
                temp_inv[x].remove([y, c])
                temp_inv[y].append([x, c])
                # x출발 y도착 edge 추가/y출발 x도착 edge 제거
                temp[x].append([y, c])
                temp[y].remove([x, c])

            for y, c in adj_lst[x]:
                #Outgoing Edges
                temp_inv[y].remove([x, c])
                temp_inv[x].append([y, c])
                # y도착 x출발 edge 제거
                temp[y].append([x, c])
                temp[x].remove([y, c])
                # y출발 x도착 edge 추가

            adj_lst, adj_lst_inv = temp, temp_inv

        for y, cost in adj_lst[x]:
            if distance[x] + cost < distance[y]:
                distance[y] = distance[x] + cost

            if not visited[x][y]:
                visited[x][y] = 1
                queue.append(y)

    print(distance)

    return distance[end]



n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]
print(solution(n, start, end, roads, traps))