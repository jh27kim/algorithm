from collections import defaultdict


def solution(land, P, Q):
    N = len(land)
    blocks = defaultdict(int)

    for i in range(N):
        for j in range(N):
            blocks[land[i][j]] += 1

    def cal(k):
        p, q = 0, 0
        for key, value in blocks.items():
            if key < k:
                p += (k - key) * value
            elif key > k:
                q += (key - k) * value

        return p * P + q * Q

    bottom = min(blocks)
    top = max(blocks)
    while True:
        mid = (bottom + top) // 2

        upperBound = cal(mid + 1)
        cur = cal(mid)
        lowerBound = cal(mid - 1)

        if cur <= lowerBound and cur <= upperBound:
            answer = cur
            break

        elif lowerBound < cur:
            top = mid - 1

        elif upperBound < cur:
            bottom = mid + 1

    return answer


