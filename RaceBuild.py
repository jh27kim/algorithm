from collections import deque
MOVEMENT = [[0, 1], [-1, 0], [0, -1], [1, 0]]
STRAIGHT = 100
CORNER = 500
answer = int(1e9)

def findCost(path):
    corner = 0
    for i in range(1, len(path)-1):
        if path[i][2] != path[i+1][2]:
            corner += 1

    return (len(path)-1)*100 + corner*CORNER


def dfs(queue, N, visited):
    global answer

    if queue[-1][0] == N-1 and queue[-1][1] == N-1:
        answer = min(answer, findCost(queue))
        return

    x, y, d = queue[-1]
    for m in range(4):
        M = MOVEMENT[m]
        nx, ny = x + M[0], y + M[1]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and not board[nx][ny]:
                queue.append([nx, ny, m])
                visited[nx][ny] = 1
                dfs(queue, N, visited)
                visited[nx][ny] = 0
                queue.pop()


def solution(board):
    global answer
    start = [0, 0, -1]
    N = len(board)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[0][0] = 1

    queue = deque()
    queue.append(start)

    dfs(queue, N, visited)

    return answer


board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]

import numpy as np
print(np.asarray(board))
print(solution(board))