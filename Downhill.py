import sys

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
DP = [[-1] * M for _ in range(N)]
MOVEMENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]
sys.setrecursionlimit(250000)


def dfs(x, y):
    if x == N - 1 and y == M - 1:
        return 1

    if DP[x][y] != -1:
        return DP[x][y]

    DP[x][y] = 0
    for m in MOVEMENT:
        nx, ny = x + m[0], y + m[1]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] < board[x][y]:
                DP[x][y] += dfs(nx, ny)

    return DP[x][y]


print(dfs(0, 0))

