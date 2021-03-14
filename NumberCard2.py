from bisect import bisect_left, bisect_right

N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
query = list(map(int, input().split()))

for q in query:
    print(bisect_right(cards, q) - bisect_left(cards, q), end=" ")

l = [2, 4, 5, 6, 6, 6, 9]
print(bisect_left(l, 6))
print(bisect_right(l, 6))