def solution(strs, t):
    MAX = int(1e9)
    n = len(t)
    dp = [MAX] * (n + 1)
    dp[0] = 0
    strs = set(strs)

    for i in range(1, n + 1):
        for k in range(1, 6):
            if i - k < 0:
                s = 0
            else:
                s = i - k
            if t[s:i] in strs:
                dp[i] = min(dp[i], dp[i - k] + 1)

    return dp[-1] if dp[-1] != MAX else -1
