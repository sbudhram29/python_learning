def greatest_rectangle(A):
    if not len(A):
        return 0

    H = []
    P = []
    max_size = float('-inf')
    h_pos_start = 0

    for i, h in enumerate(A):
        if not len(H) or h > H[-1]:
            H.append(h)
            P.append(i)
        elif h < H[-1]:
            while len(H) and h < H[-1]:
                h_pos_start, max_size = get_max_p(H, P, max_size, i)

            # save max height, and first index of height
            H.append(h)
            P.append(h_pos_start)

    while len(H):
        h_pos_start, max_size = get_max_p(H, P, max_size, i + 1)

    return max_size

def get_max_p(H, P, m, p):
    temp_h = H.pop()
    temp_p = P.pop()

    temp_m = temp_h * (p - temp_p)

    return temp_p, max(m, temp_m)


H = [5,6,4,1,9,7,5, 3]

print(greatest_rectangle(H))