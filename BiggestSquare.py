import math

def solution(board):
    N, M = len(board), len(board[0])
    dp = [[0 for _ in range(M)] for _ in range(N)]
    for x in range(N):
        dp[x][0] = board[x][0]
    for y in range(M):
        dp[0][y] = board[0][y]

    for i in range(1, N):
        for j in range(1, M):
            if board[i][j]:
                dp[i][j] = int(math.sqrt((min(dp[i-1][j-1], min(dp[i][j-1], dp[i-1][j])))) + 1) ** 2
                #print(dp, i, j)

    answer = 0
    for i in range(N):
        for j in range(M):
            answer = max(answer, dp[i][j])

    return answer


board = [[0,0,1,1],[1,1,1,1]]
print(solution(board))