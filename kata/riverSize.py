from collections import deque
def river_size(river):
    if not river:
        return 0

    sizes = []

    visited = []
    for _ in river:
        temp = []
        for _ in river[0]:
            temp.append(False)

        visited.append(temp)

    for i,_ in enumerate(river):
        for j,_ in enumerate(river[i]):
            if visited[i][j]:
                continue

            traverse_river(i, j, river, visited, sizes)

    return sizes

def traverse_river(i, j, river, visited, sizes):
    size = 0
    q = deque([])

    q.append([i,j])

    while len(q):
        row, col = q.popleft()

        if visited[row][col]:
            continue

        visited[row][col] = True

        if river[row][col] == 0:
            continue

        size += 1

        neighbors = get_neighbors(row, col, river, visited)

        for n in neighbors:
            q.append(n)

    if size > 0:
        sizes.append(size)

def get_neighbors(row, col, river, visited):
    neighbors = []

    if row > 0 and not visited[row - 1][col]:
        neighbors.append([row-1, col])

    if row < len(river) - 1  and not visited[row + 1][col]:
         neighbors.append([row + 1, col])

    if col > 0 and not visited[row][col -1]:
        neighbors.append([row, col - 1])

    if col < len(river[0]) - 1 and not visited[row][col + 1]:
        neighbors.append([row, col + 1])

    return neighbors

print(river_size([[1,1,1,0,0,],[0,0,1,1,0,]]))