from collections import deque


def solution(k, num, links):
    answer = 0
    total = num
    indegree = [0 for _ in range(len(num))]
    parents = [-1 for _ in range(len(num))]

    for i in range(len(links)):
        x, y = links[i]
        ind = 0
        if x != -1:
            ind += 1
            parents[x] = i

        if y != -1:
            ind += 1
            parents[y] = i
        indegree[i] = ind

    queue = deque()
    for i in range(len(indegree)):
        if not indegree[i]:
            queue.append(i)

    while queue:
        x = queue.popleft()
        if parents[x] == -1:
            break
        total[parents[x]] += total[x]
        queue.append(parents[x])


    return answer


k = 2
num = [6, 9, 7, 5]
links = [[-1, -1], [-1, -1], [-1, 0], [2, 1]]
print(solution(k, num, links))
