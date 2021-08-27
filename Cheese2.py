from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
MOVEMENT = [[0, -1], [0, 1], [1, 0], [-1, 0]]
START = [0, 0]


def return_queue():
    q = deque()
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append(START)

    while queue:
        x, y = queue.popleft()
        for m in MOVEMENT:
            nx, ny = x + m[0], y + m[1]
            if 0 <= nx < N and 0 <= ny < M and not board[nx][ny]:
                if not visited[nx][ny]:
                    queue.append([nx, ny])
                    q.append([nx, ny])
                    visited[nx][ny] = 1
    return q


def bfs(queue):
    newboard = [[0 for _ in range(M)] for _ in range(N)]
    while queue:
        x, y = queue.popleft()
        for m in MOVEMENT:
            nx, ny = x + m[0], y + m[1]
            if 0 <= nx < N and 0 <= ny < M:
                newboard[nx][ny] += 1

    for i in range(N):
        for j in range(M):
            if board[i][j] and newboard[i][j] >= 2:
                board[i][j] = 0


def check(board):
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                return True
    return False


answer = 0
#import numpy as np
while check(board):
    #print(np.array(board))
    queue = return_queue()
    bfs(queue)
    answer += 1

print(answer)
