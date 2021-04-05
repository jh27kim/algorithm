def dp(sticker, N):
    DP = [0] * N
    DP[0] = sticker[0]
    DP[1] = max(sticker[0], sticker[1])

    for i in range(2, len(sticker)):
        DP[i] = max(DP[i - 2] + sticker[i], DP[i - 1])

    return DP[-1]


def solution(sticker):
    N = len(sticker) - 1
    if N >= 2:
        return max(dp(sticker[1:], N), dp(sticker[:-1], N))
    else:
        if N == 0:
            return sticker[0]
        else:
            return max(sticker[0], sticker[1])