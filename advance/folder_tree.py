arr = [
    'home',
    'home/user',
    'home/user/id',
    'videos',
    'videos/user',
    'videos/user/id'
]

routes = {}

for uri in arr:
    current = routes
    for segs in uri.split('/'):
        if segs in current:
            current = current[segs]
        else:
            current[segs] = {}


def printTree(routes, delimeter):
    delimeter = ' ' + delimeter

    for route in routes:
        print(delimeter + route)
        if type(routes[route]) == dict:
            printTree(routes[route], delimeter)


printTree(routes, '-')
