from collections import deque


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
MOVEMENT = [[0, 1], [-1, 0], [0, -1], [1, 0]]
queue = []
temp = []

for i in range(N):
    for j in range(N):
        if board[i][j]:
            queue.append([i, j, board[i][j]])

queue.sort(key=lambda x:x[-1], reverse=True)

for _ in range(S):
    queue.sort(key=lambda x:x[-1], reverse=True)
    while queue:
        x, y, virus = queue.pop()
        for m in MOVEMENT:
            nx, ny = x + m[0], y + m[1]
            if 0 <= nx < N and 0 <= ny < N:
                if not board[nx][ny]:
                    board[nx][ny] = virus
                    temp.append([nx, ny, virus])
    queue = temp
    temp = []

print(board[X-1][Y-1])
