def walls(M):
    if not len(M):
        return

    visited = [[False for _ in row] for row in M]

    for r in range(len(M)):
        for c in range(len(M[0])):
            if M[r][c] == -2:
                visited[r][c] = True
                dfs(r - 1,c,M, visited, 1)
                dfs(r + 1,c,M, visited, 1)
                dfs(r,c -1 ,M, visited, 1)
                dfs(r,c + 1,M, visited, 1)
                visited[r][c] = False

    return M


def dfs(r, c, M, visited, level):

    if not is_safe(r,c,M, visited):
        return

    if M[r][c] == 0 or M[r][c] > level:
        M[r][c] = level

    visited[r][c] = True
    dfs(r - 1, c, M, visited, level +1)
    dfs(r + 1, c, M, visited, level +1)
    dfs(r, c - 1, M, visited, level +1)
    dfs(r, c + 1, M, visited, level +1)
    visited[r][c] = False

def is_safe(r,c,M,visited):

    if r < 0 or c < 0 or c >= len(M[0]) or r >= len(M) or visited[r][c] or M[r][c] == -1:

        return False

    return True


m = [
    [0, 0, 0, 0, -1, 0, -2],
    [-2, 0, 0, 0, 0, 0, 0],
]

print(walls(m))