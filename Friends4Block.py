import copy

answer = 0
MOVEMENT = [[0, 0], [0, 1], [1, 0], [1, 1]]


def check(board):
    global answer
    newboard = copy.deepcopy(board)
    removed = False

    for i in range(len(board) - 1):
        for j in range(len(board[0]) - 1):
            if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1] != 0:
                for m in range(4):
                    ni, nj = i + MOVEMENT[m][0], j + MOVEMENT[m][1]
                    if newboard[ni][nj] != 0:
                        newboard[ni][nj] = 0
                        answer += 1
                removed = True

    b = []
    # print(len(board), len(board[0]))
    for c in range(len(board[0])):
        temp = []
        for r in range(len(board) - 1, -1, -1):
            if newboard[r][c] != 0:
                temp.append(newboard[r][c])

        while len(temp) != len(board):
            temp.append(0)
        b.append(temp[::-1])

    return removed, list(map(list, zip(*b)))


def solution(m, n, board):
    global answer
    for r in range(m):
        board[r] = list(board[r])

    while True:
        bit, board = check(board)

        #print(board)
        if not bit:
            break

    return answer


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m, n, board))