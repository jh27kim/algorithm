from collections import deque

MOVEMENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]
MAX = int(1e9)


def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]


def union(parents, x, y):
    a = find(parents, x)
    b = find(parents, y)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def bfs(board, area, cnt):
    N = len(board)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    distance = [[MAX for _ in range(cnt)] for _ in range(cnt)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                for M in MOVEMENT:
                    ni, nj = i + M[0], j + M[1]
                    if 0 <= ni < N and 0 <= nj < N:
                        if area[i][j] != area[ni][nj]:
                            a = area[i][j]
                            b = area[ni][nj]
                            if abs(board[ni][nj] - board[i][j]) < distance[min(a, b) - 1][max(a, b) - 1]:
                                distance[min(a, b) - 1][max(a, b) - 1] = abs(board[ni][nj] - board[i][j])
    return distance


def solution(land, height):
    answer = 0
    N = len(land)
    visited = [[False for _ in range(N)] for _ in range(N)]
    area = [[0 for _ in range(N)] for _ in range(N)]

    cnt = 1
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                queue = deque()
                queue.append([i, j])
                while queue:
                    x, y = queue.popleft()
                    visited[x][y] = 1
                    area[x][y] = cnt
                    for M in MOVEMENT:
                        nx, ny = x + M[0], y + M[1]
                        if 0 <= nx < N and 0 <= ny < N:
                            if abs(land[nx][ny] - land[x][y]) <= height and not visited[nx][ny]:
                                queue.append([nx, ny])
                cnt += 1

    parents = [i for i in range(cnt - 1)]
    adj_lst = bfs(land, area, cnt - 1)
    edges = []
    for n in range(cnt - 1):
        for m in range(n + 1, cnt - 1):
            if adj_lst[n][m] != MAX:
                edges.append([adj_lst[n][m], n, m])

    edges.sort(reverse=True)
    c = 0

    while c != cnt - 1 and edges:
        dist, a, b = edges.pop()
        if find(parents, a) != find(parents, b):
            union(parents, a, b)
            answer += dist
            c += 1

    return answer

'''Using Heapq'''
import heapq


def solution2(land, height):
    N = len(land)
    visited = [[False for _ in range(N)] for _ in range(N)]
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = []

    queue.append((0, 0, 0))
    visit_count = 0
    max_count = N * N
    value = 0

    while (visit_count < max_count):
        v, y, x = heapq.heappop(queue)
        if visited[y][x]:
            continue
        visited[y][x] = True

        visit_count += 1
        value += v

        c_height = land[y][x]
        for ay, ax in move:
            ny, nx = y + ay, x + ax
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                n_height = land[ny][nx]

                if abs(n_height - c_height) > height:
                    heapq.heappush(queue, (abs(n_height - c_height), ny, nx))
                else:
                    heapq.heappush(queue, (0, ny, nx))
    return value


land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
height = 3
print(solution2(land, height))