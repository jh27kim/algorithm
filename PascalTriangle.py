T = int(input())

prev = [1]
END = 1

for t in range(1, T+1):
    N = int(input())
    print("#" + str(t))
    for i in range(1, N + 1):
        if i == 1:
            print(1)
        elif i == 2:
            print(END, end=" ")
            print(END)

            prev = [1, 1]

        else:
            newlst = [1]
            for j in range(len(prev) - 1):
                newlst.append(prev[j + 1] + prev[j])
            newlst.append(1)
            print(*newlst, end=" ")
            #print(newlst)
            print()
            prev = newlst

