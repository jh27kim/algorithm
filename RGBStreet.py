N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]


def solution(N, cost):
    answer = int(1e9)

    for c in range(3):
        dp = [[-1 for _ in range(3)] for _ in range(N)]
        for i in range(3):
            if i == c:
                dp[0][i] = cost[0][i]
                continue
            dp[0][i] = int(1e9)

        for i in range(1, N):
            dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = cost[i][2] + min(dp[i-1][1], dp[i-1][0])

        for i in range(3):
            if i == c:
                continue
            answer = min(answer, dp[-1][i])

    return answer


print(solution(N, cost))
