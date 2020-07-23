def walls(M):
    if not M:
        return 0

    visited = [[False for _ in row] for row in M]

    for row in range(len(M)):
        for col in range(len(M[row])):
            if M[row][col] == -2:
                visited[row][col] = True
                dfs(M, row - 1, col, 1, visited)
                dfs(M, row + 1, col, 1, visited)
                dfs(M, row, col - 1, 1, visited)
                dfs(M, row, col + 1, 1, visited)
                visited[row][col] = False

    return M



def dfs(M, row, col, depth, visited):

    if not is_safe(M, row, col, visited):
       return


    if M[row][col] == 0 or M[row][col] > depth:
        M[row][col] = depth

    visited[row][col] = True

    dfs(M, row - 1, col, depth + 1, visited)
    dfs(M, row + 1, col, depth + 1, visited)
    dfs(M, row, col - 1, depth + 1, visited)
    dfs(M, row, col + 1, depth + 1, visited)

    visited[row][col] = False

def is_safe(M, row, col, visited):

    if row < 0 or col < 0 or col >= len(M[0]) or row >= len(M) or visited[row][col] or M[row][col] == -1:
        return False

    return True


print(walls([[0,0,-2],[0,0,0]]))
print(walls([[0,0,-2, -1, 0, 0],[0,0,0,0,0,0], [0,0,0,0,0,0],[0,0,0,0,0,-2]]))
