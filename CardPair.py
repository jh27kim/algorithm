from itertools import permutations
import copy
from collections import deque

MOVEMENT = [[1, 0], [0, -1], [-1, 0], [0, 1]]
MAX = 17


def move(start, end, new_board):
    distance = [[MAX for _ in range(4)] for _ in range(4)]
    distance[start[0]][start[1]] = 0

    start = copy.deepcopy(start)
    start.append(0)
    queue = deque()
    queue.append(start)

    while queue:
        x1, y1, d = queue.popleft()
        if distance[x1][y1] < d:
            continue

        for M in MOVEMENT:
            nx, ny = x1 + M[0], y1 + M[1]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if distance[nx][ny] > d+1:
                    distance[nx][ny] = d+1
                    queue.append([nx, ny, d+1])

                while 0 <= nx + M[0] < 4 and 0 <= ny + M[1] < 4 and not new_board[nx + M[0]][ny + M[1]]:
                    nx += M[0]
                    ny += M[1]

                if distance[nx][ny] > d + 1:
                    distance[nx][ny] = d + 1
                    queue.append([nx, ny, d + 1])

    return distance[end[0]][end[1]]


def move_count(permutation, board, begin):
    res = int(1e9)
    for perm in permutation:
        new_board = copy.deepcopy(board)
        temp = move(begin, perm[0][0], new_board)

        for x, y in perm:
            temp += move(x, y, new_board)
            new_board[x[0]][x[1]] = 0
            new_board[y[0]][y[1]] = 0

        res = min(res, temp)

    return res


def solution(board, r, c):
    answer = int(1e9)
    cards = [[] for _ in range(6)]
    card_numbers = 0

    for i in range(4):
        for j in range(4):
            if board[i][j]:
                card_numbers += 1
                cards[board[i][j]-1].append([i, j])

    cards1 = []
    cards2 = []

    for card in cards:
        if card:
            cards1.append(card)
            cards2.append(card[::-1])

    answer = min(move_count(list(permutations(cards1)), board, [r, c]), answer)
    answer = min(move_count(list(permutations(cards2)), board, [r, c]), answer)

    return answer + card_numbers


board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
r = 0
c = 1
print(solution(board, r, c))