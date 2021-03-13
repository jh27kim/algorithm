T = int(input())
for _ in range(T):
    N = int(input())
    tree = [0 for _ in range(N+1)]

    for _ in range(N-1):
        p, c = map(int, input().split())
        tree[c] = p

    a, b = map(int, input().split())

    a_parents = [a]
    b_parents = [b]

    while tree[a]:
        a_parents.append(tree[a])
        a = tree[a]

    while tree[b]:
        b_parents.append(tree[b])
        b = tree[b]

    a_level = len(a_parents) - 1
    b_level = len(b_parents) - 1
    while a_parents[a_level] == b_parents[b_level]:
        a_level -= 1
        b_level -= 1

    print(a_parents[a_level+1])
