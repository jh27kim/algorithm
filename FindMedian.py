import heapq
import sys

N = int(input())
left, right = [], []
answer = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if len(right) >= 1:
        if -left[0] > right[0]:
            leftMAX = -heapq.heappop(left)
            rightMIN = heapq.heappop(right)
            heapq.heappush(left, -rightMIN)
            heapq.heappush(right, leftMAX)

    answer.append(-left[0])

print(*answer, sep="\n")
