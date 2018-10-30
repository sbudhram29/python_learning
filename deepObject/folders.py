routes = [
    'home',
    'home/user',
    'home/user/id',
    'videos',
    'videos/genre',
    'videos/genre/kids',
]

list_of_routes = {}

for route in routes:
    current = list_of_routes
    for r in route.split('/'):
        if r not in current:
            current[r] = {}
        current = current[r]


def printRoutes(routes, delimeter):
    for k, v in routes.items():
        print(delimeter + k)
        if type(v) == dict:
            printRoutes(v, ' ' + delimeter)


printRoutes(list_of_routes, '-')
