folders = [
    'home',
    'home/user',
    'home/user/id',
    'home/user/classes',
    'home/videos',
    'home/videos/id',
    'work',
    'work/user',
    'work/user/id',
    'work/user/classes',
    'work/videos',
    'work/videos/id',
]

tree_struct = {}

for folder in folders:
    folderArr = folder.split('/')

    current = tree_struct

    for branch in folderArr:
        current[branch], current = current.get(
            branch, {}), current.get(branch, current)


def printRoutes(routes, delimeter):
    for k, v in routes.items():
        print(delimeter + k)
        if type(v) is dict:
            printRoutes(v, ' ' + delimeter)


printRoutes(tree_struct, '-')
