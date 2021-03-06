MOVEMENT = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]


def deploy(queen, num, N):
    x, y = queen
    board[x][y] += num
    for M in MOVEMENT:
        nx, ny = x, y
        while 0 <= nx + M[0] < N and 0 <= ny + M[1] < N:
            nx += M[0]
            ny += M[1]
            board[nx][ny] += num


def dfs(N, depth, x, k):
    global answer

    if depth == n:
        answer += 1
        return

    for i in range(x, N):
        if x == i:
            y = k
        else:
            y = 0

        for j in range(y, N):
            if not board[i][j]:
                deploy([i, j], 1, N)
                dfs(N, depth+1, i, j+1)
                deploy([i, j], -1, N)


def sol(n):
    global answer, board
    answer = 0
    board = [[0 for _ in range(n)] for _ in range(n)]

    dfs(n, 0, 0, 0)

    return answer


n = 4
print(sol(n))