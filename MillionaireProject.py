T = int(input())

for n in range(1, T + 1):
    N = int(input())
    days = list(map(int, input().split()))
    answer = 0
    cnt = 0
    accum = 0
    price = days[-1]

    for day in days[-2::-1]:
        if day < price:
            answer += price - day
        else:
            price = day


    print("#" + str(n), answer)
