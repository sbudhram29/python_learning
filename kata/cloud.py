def jumping_on_clouds(c):

    l = len(c)

    step = 0
    jumps = -1
    while step < l:
        if step + 2 < l and c[step + 2] == 0:
            step += 1
        jumps += 1
        step += 1

    return jumps


print(jumping_on_clouds([0, 0, 1, 0, 0, 1, 0]))
print(jumping_on_clouds([0, 0, 0, 1, 0, 0]))
