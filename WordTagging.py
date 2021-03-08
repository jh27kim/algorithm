def solution(n, words):
    answer = [0, 0]
    spoken = set()

    for i in range(len(words)):
        if i >= 1:
            if words[i][0] != words[i - 1][-1]:
                print(i)
                q, r = divmod(i, n)
                answer = [r + 1, q + 1]
                break

        if words[i] in spoken:
            print(i)
            q, r = divmod(i, n)
            answer = [r + 1, q + 1]
            break
        spoken.add(words[i])

    return answer