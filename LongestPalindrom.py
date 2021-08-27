def solution(s):
    answer = ""

    if len(s) < 2 or s == s[::-1]:
        return len(s)

    def twopointer(l, h):
        while l >= 0 and h <= len(s) and s[l] == s[h - 1]:
            l -= 1
            h += 1

        return s[l + 1:h - 1]

    for i in range(len(s)):
        answer = max(answer,
                     twopointer(i, i + 1),
                     twopointer(i, i + 2),
                     key=len)

    return len(answer)


