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
            current[seg] = current.get(seg, {})
            current = current[seg]

    return routes


print(get_routes(list_of_uri))


def print_routes(routes, delimiter):
    for route in routes:
        print(delimiter + route)
        if type(routes[route]) is dict:
            print_routes(routes[route], ' ' + delimiter)


print_routes(get_routes(list_of_uri), '->')
