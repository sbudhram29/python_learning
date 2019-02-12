def jumpingOnclouds(c):

    l = len(c)

    step = 0
    jumps = -1
    while step < l:
        if step + 2 < l and c[step + 2] == 0:
            step += 1
        jumps += 1
        step += 1

    return jumps


print(jumpingOnclouds([0, 0, 1, 0, 0, 1, 0]))
print(jumpingOnclouds([0, 0, 0, 1, 0, 0]))
