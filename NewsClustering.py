from collections import Counter


def multipleSet(string):
    newString = []
    for i in range(len(string) - 1):
        if string[i].isalpha() and string[i + 1].isalpha():
            newString.append(string[i].lower() + string[i + 1].lower())

    return newString


def solution(str1, str2):
    answer = 0
    A = Counter(multipleSet(str1))
    B = Counter(multipleSet(str2))

    up, down = 0, 0
    if len(A) == 0 and len(B) == 0:
        return 65536
    elif len(A) == 0 or len(B) == 0:
        return 0

        # print(A, B)

    for k, v in A.items():
        if k in B:
            up += min(v, B[k])
            down += max(v, B[k])
        else:
            down += v

    for k, v in B.items():
        if k not in A:
            down += v

    return int(up / down * 65536)
