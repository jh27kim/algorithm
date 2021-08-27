from collections import deque

MOVEMENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def bfs(x, y):
    queue = deque()
    queue.append(x)
    distance = 0
    visited = [[0 for _ in range(3)] for _ in range(4)]

    while queue:
        lenq = len(queue)

        while lenq:
            print(queue)
            n, m = queue.popleft()
            if [n, m] == y:
                return distance
            for dx, dy in MOVEMENT:
                nx, ny = n + dx, m + dy
                if 0 <= nx < 4 and 0 <= ny < 3 and not visited[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
            lenq -= 1
        distance += 1


def solution(numbers, hand):
    answer = ''
    left, right = 10, 12
    hand = "L" if hand == "left" else "R"

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = number
        elif number in [3, 6, 9]:
            answer += 'R'
            right = number
        else:
            if number == 0: number = 11
            leftDistance = bfs([(left - 1) // 3, (left - 1) % 3], [(number - 1) // 3, (number - 1) % 3])
            rightDistance = bfs([(right - 1) // 3, (right - 1) % 3], [(number - 1) // 3, (number - 1) % 3])
            print(left, right, number, leftDistance, rightDistance)
            if leftDistance < rightDistance:
                answer += 'L'
                left = number
            elif rightDistance < leftDistance:
                answer += 'R'
                right = number
            else:
                answer += hand
                if hand == 'L':
                    left = number
                else:
                    right = number
    return answer


numbers = [0]
hand = "right"
print(solution(numbers, hand))