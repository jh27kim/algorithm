from collections import defaultdict


def solution(gems):
    answer = [0, len(gems)]
    start, end = 0, 0
    TOTAL_GEMS = len(set(gems))
    bag = defaultdict(int)

    while True:
        if start == len(gems):
            break

        if len(bag) == TOTAL_GEMS:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]

            if bag[gems[start]] == 1:
                del bag[gems[start]]

            else:
                bag[gems[start]] -= 1

            start += 1
            continue

        if end == len(gems):
            break

        if len(bag) != TOTAL_GEMS:
            bag[gems[end]] += 1
            end += 1
            print(end)
            continue

    return [answer[0] + 1, answer[1]]


gems = ["ZZZ", "YYY", "NNNN", "AAA", "BBB"]
print(solution(gems))
