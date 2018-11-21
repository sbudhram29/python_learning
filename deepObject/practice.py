list_of_uri = [
    'home',
    'home/user',
    'home/user/id',
    'videos',
    'videos/id',
    'videos/user',
    'videos/user/id',
]


def get_routes(uris):
    routes = {}
    for uri in uris:
        segs = uri.split('/')
        current = routes

        for seg in segs:
            if current.get(seg) != None:
                current = current[seg]
            else:
                current[seg] = {}

    return routes


print(get_routes(list_of_uri))


def print_routes(routes, delimeter):
    for route in routes:
        print(delimeter + route)
        if type(routes[route]) == dict:
            print_routes(routes[route], ' ' + delimeter)


print_routes(get_routes(list_of_uri), '->')
