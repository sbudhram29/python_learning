def greater_rectangle(A):

    max_size = float('-inf')
    p = 0
    h_stack = []
    p_stack = []

    for i,_ in enumerate(A):
        h = A[i]
        if (len(h_stack) == 0 or h > h_stack[-1]):
            h_stack.append(h)
            p_stack.append(i)

        elif h < h_stack[-1]:
            while len(h_stack) and h < h_stack[-1]:
                p, max_size = get_next(h_stack, p_stack, max_size, i)

            h_stack.append(h)
            p_stack.append(p)

        print(h, i, p, h_stack, p_stack, max_size)

    while len(h_stack):
        p, max_size = get_next(h_stack, p_stack, max_size, len(A))

    return max_size


def get_next(h_stack, p_stack, max_size, pos):
    temp_h = h_stack.pop()
    temp_p = p_stack.pop()

    temp_size = temp_h * (pos-temp_p)
    print(temp_size, f"{temp_h} * ({pos} - {temp_p})")
    max_size = max(temp_size, max_size)

    return temp_p, max_size


H = [5,6,4,1,9,7,5, 3]

print(greater_rectangle(H))