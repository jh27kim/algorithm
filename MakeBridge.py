from collections import deque
import sys

MAX = sys.maxsize
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
MOVEMENT = [[0, 1], [-1, 0], [0, -1], [1, 0]]


def bfs(queue, mark, visited):
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        board[x][y] = mark
        for m in MOVEMENT:
            nx, ny = x + m[0], y + m[1]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    board[nx][ny] = mark


def findPath(adj_lst):
    for x in range(N):
        for y in range(M):
            if board[x][y]:
                for m in MOVEMENT:
                    nx, ny = x, y
                    while 0 <= nx + m[0] < N and 0 <= ny + m[1] < M:
                        nx += m[0]
                        ny += m[1]
                        if board[nx][ny] == board[x][y]:
                            break

                        if board[nx][ny] and board[nx][ny] != board[x][y]:
                            if board[nx-m[0]][ny-m[1]] == board[nx][ny]:
                                continue
                            cost = abs(nx - x) + abs(ny - y) - 1
                            if 2 <= cost < adj_lst[board[x][y]-1][board[nx][ny]-1]:
                                #print('start:', [x, y] , board[x][y], '--> end', [nx, ny], board[nx][ny])
                                #print(cost)
                                #print()
                                adj_lst[board[x][y] - 1][board[nx][ny] - 1] = cost
                                #adj_lst[board[nx][ny] - 1][board[x][y] - 1] = cost
                                #break


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]


mark = 0
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] and not visited[i][j]:
            mark += 1
            bfs(deque([[i, j]]), mark, visited)

#import numpy as np
#print(np.asarray(board))

adj_lst = [[int(10000) for j in range(mark)] for i in range(mark)]

findPath(adj_lst)
#print(np.asarray(adj_lst))

parent = [i for i in range(mark)]
distances = []

for i in range(mark):
    for j in range(i, mark):
        if adj_lst[i][j] != 10000:
            distances.append([adj_lst[i][j], i, j])

distances.sort()
answer = 0
check = [0 for _ in range(mark)]

for d, x, y in distances:
    if find(parent, x) != find(parent, y):
        answer += d
        union(parent, x, y)
        check[x], check[y] = 1, 1

if sum(check) == mark:
    print(answer)
else:
    print(-1)
