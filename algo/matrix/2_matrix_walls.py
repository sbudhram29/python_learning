m = [
    [0, 0, 0, 0, -1, 0, -2],
    [-2, 0, 0, 0, 0, 0, 0],
]

def walls(M):
    if not M:
        return

    visited = [[False for _ in row] for row in M]

    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == -2:
                visited[i][j] = True
                update_distance(i + 1, j, M, visited, 1)
                update_distance(i - 1, j, M, visited, 1)
                update_distance(i, j + 1, M, visited, 1)
                update_distance(i, j - 1, M, visited, 1)
                visited[i][j] = False

    return M

def update_distance(i, j, M, visited, depth):
    if not is_safe(i, j, M, visited):
        return

    if M[i][j] == 0 or M[i][j] > depth:
        M[i][j] = depth

    visited[i][j] = True

    update_distance(i + 1, j, M, visited, depth + 1)
    update_distance(i - 1, j, M, visited, depth + 1)
    update_distance(i, j + 1, M, visited, depth + 1)
    update_distance(i, j - 1, M, visited, depth + 1)

    visited[i][j] = False


def is_safe(i, j, M, visited):

    # boundary checking, keep in mind
    if i < 0 or i >= len(M) or j < 0 or j >= len(M[0]):
        return False

    # checking for either walls or -2 or if visited
    if M[i][j] == -1 or M[i][j] == -2 or visited[i][j]:

        return False

    return True


print(walls(m))