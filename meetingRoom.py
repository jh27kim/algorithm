from collections import deque


MOVEMENT = [[0, 1], [-1, 0], [0, -1], [1, 0]]


def manhattan(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def initial(board):
    person = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'P':
               person.append([i, j])
    return person


def solution(places):
    answer = []
    for board in places:
        ppl = initial(board)
        obeyed = True

        for p in ppl:
            queue = deque()
            queue.append(p)
            visited = [[0 for _ in range(5)] for _ in range(5)]
            dist = [[0 for _ in range(5)] for _ in range(5)]

            while queue:
                x, y = queue.popleft()
                visited[x][y] = 1
                for M in MOVEMENT:
                    nx, ny = x + M[0], y + M[1]
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if board[nx][ny] != 'X' and not visited[nx][ny]:
                            queue.append([nx, ny])
                            visited[nx][ny] = 1
                            dist[nx][ny] = dist[x][y] + 1

            #print(dist)
            for i, j in ppl:
                if [i, j] == p:
                    continue
                if 0 < dist[i][j] <= 2:
                    obeyed = False
                    break

            if not obeyed:
                answer.append(0)
                break

        if obeyed:
            answer.append(1)

    return answer





places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))