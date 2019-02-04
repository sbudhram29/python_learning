routes = [
    'home',
    'home/user',
    'home/user/id',
    'videos',
    'videos/genre',
    'videos/genre/kids',
    'home/user/videos/games',
]

list_of_routes = {}

for route in routes:
    current = list_of_routes
    for r in route.split('/'):
        # assign current[r] to current[r] or create new dict
        current[r] = current.get(r, {})
        # move current to current[r] for nesting
        current = current[r]


def printRoutes(routes, delimeter):
    for k, v in routes.items():
        print(delimeter + k)
        if isinstance(v, dict):
            printRoutes(v, ' ' + delimeter)


printRoutes(list_of_routes, '-')
print(list_of_routes['home']['user']['videos'].get('games'))
