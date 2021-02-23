gear = []
for _ in range(4):
    g = list(input())
    gear.append(g)
K = int(input())
LEFT, RIGHT = 6, 2


def rotate(direction):
    for i in range(4):
        if direction[i] == 0:
            continue

        if direction[i] == 1:
            gear[i] = [gear[i][-1]] + gear[i][:-1]

        elif direction[i] == -1:
            gear[i] = gear[i][1:] + [gear[i][0]]


for _ in range(K):
    gearNumber, rotation = map(int, input().split())
    gearNumber -= 1

    direction = [0 for _ in range(4)]
    direction[gearNumber] = rotation

    if gearNumber == 0:
        for i in range(3):
            if gear[i][RIGHT] != gear[i+1][LEFT]:
                direction[i+1] = -(direction[i])
            else:
                break

    elif gearNumber == 3:
        for i in range(3, 0, -1):
            if gear[i][LEFT] != gear[i-1][RIGHT]:
                direction[i-1] = -(direction[i])
            else:
                break
    else:
        for i in range(gearNumber, 3):
            if gear[i][RIGHT] != gear[i+1][LEFT]:
                direction[i+1] = -(direction[i])
            else:
                break

        for i in range(gearNumber, 0, -1):
            if gear[i][LEFT] != gear[i - 1][RIGHT]:
                direction[i-1] = -(direction[i])
            else:
                break

    #print(direction)
    rotate(direction)
    #print(gear)

answer = 0
for i in range(4):
    if gear[i][0] == '0':
        continue
    else:
        answer += pow(2, i)

print(answer)
