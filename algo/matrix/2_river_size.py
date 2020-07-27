def river_size(M):
    if not M:
        return

    V = [[False for _ in r] for r in M]
    S = []

    for r in range(len(M)):
        for c in range(len(M[0])):
            if V[r][c]:
                continue

            traverse_river(r,c, M, V, S)

    return S

def traverse_river(r,c, M, V, S):
    size = 0

    Q = [[r,c]]

    while len(Q):
        [r,c] = Q.pop(0)

        if V[r][c]:
            continue

        V[r][c] = True

        if M[r][c] == 0:
            continue

        size += 1

        N = get_neighbors(r, c, M, V)

        for n in N:
            Q.append(n)


    if size > 0:
        S.append(size)


def get_neighbors(r, c, M, V):
    neighbors = []

    if r > 0 and not V[r - 1][c]:
        neighbors.append([r - 1 ,c])

    if r < len(M) - 1 and not V[r + 1][c]:
        neighbors.append([r + 1,c])


    if c > 0 and not V[r][c -1]:
        neighbors.append([r, c -1])
    if c > len(M[0]) - 1 and not V[r ][c + 1]:
        neighbors.append([r, c + 1])


    return neighbors


R = [
    [0,0,0,0,1],
    [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1],
]

print(river_size(R))