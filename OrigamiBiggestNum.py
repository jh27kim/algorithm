answer = -1


def dfs(depth, maxdepth, paper):
    global answer

    if depth == maxdepth:
        answer = max(answer, max(paper))
        return

    for s in range(1, len(paper)):
        left = paper[:s]
        right = paper[s:]
        if len(left) < len(right):
            left = left[::-1]
            newpaper = [right[i] + left[i] for i in range(len(left))] + right[len(left):]
        else:
            #print(left, right)
            right = right[::-1]
            newpaper = left[:len(left) - len(right)] + [right[i] + left[len(left)-len(right)+i] for i in range(len(right))]
            #print(newpaper)

        dfs(depth + 1, maxdepth, newpaper)


def solution(paper, n):
    global answer
    for depth in range(n + 1):
        dfs(0, depth, paper)
    return answer


paper = [7, 3, 5, -2, 9]
n = 2
print(solution(paper, n))