arr = [
    'home',
    'home/user',
    'home/user/id',
    'home/user/id/1',
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

print(routes)


def print_tree(routes_dict, delimiter):
    delimiter = ' ' + delimiter

    for key, route in routes_dict.items():
        print(delimiter + ' ' + key)
        if type(route) is dict:
            print_tree(route, delimiter)


print_tree(routes, '->')
