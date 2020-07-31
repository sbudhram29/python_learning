def greatest_rectangle(A):
    if not len(A):
        return 0

    H = []
    P = []

    p, max_size = 0, float('-inf')

    for i, h in enumerate(A):

        if not len(H) or h > H[-1]:
            H.append(h)
            P.append(i)
        elif h < H[-1]:
            while len(H) and h < H[-1]:
                p, max_size = get_p_max(H, P, i, max_size)

            H.append(h)
            P.append(p)

    while len(H):
        p, max_size = get_p_max(H, P, i + 1, max_size)

    return max_size

def get_p_max(H, P, i, m):

    h = H.pop()
    p = P.pop()
    size = h *  (i - p)
    return p, max(size, m)

H = [5,6,4,1,9,7,5, 3]

print(greatest_rectangle(H))