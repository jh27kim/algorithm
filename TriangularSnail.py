def solution(n):
    answer = []
    triangle = [[0 for _ in range(i)] for i in range(1, n+1)]
    number = 1
    total = sum(range(1, n+1))
    loop = n
    MOVEMENT = [[1, 0], [0, 1], [-1, -1]]
    nx, ny = -1, 0
    m = 0

    while number <= total:
        for i in range(loop):
            nx += MOVEMENT[m][0]
            ny += MOVEMENT[m][1]
            triangle[nx][ny] = number
            number += 1

        loop -= 1
        m = (m+1) % 3

    for l in triangle:
        answer += l

    return answer

n = 4
print(solution(n))