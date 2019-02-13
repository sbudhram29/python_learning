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
    for seg in uri.split('/'):
        if seg in current:
            current = current[seg]
        else:
            current[seg] = {}


def print_tree(routes_dict, delimiter):
    delimiter = ' ' + delimiter

    for key, route in routes_dict.items():
        print(delimiter + ' ' + key)
        if type(route) is dict:
            print_tree(route, delimiter)


print_tree(routes, '->')
