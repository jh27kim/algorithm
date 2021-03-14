equation = input()

temp = ''
numbers = []
op = []
for s in equation:
    if s.isdigit():
        temp += s
    else:
        numbers.append(int(temp))
        op.append(s)
        temp = ''
numbers.append(int(temp))
visited = [0 for _ in range(len(numbers))]
visited[0] = 1

res = numbers[0]
for i in range(1, len(numbers)):
    if visited[i]:
        continue
    if op[i-1] == '+':
        visited[i] = 1
        res += numbers[i]
        continue
    temp = numbers[i]
    for j in range(i+1, len(numbers)):
        if op[j-1] == "+":
            temp += numbers[j]
            visited[j] = 1
            continue
        break
    res -= temp

print(res)

