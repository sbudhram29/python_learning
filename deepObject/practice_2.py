list_of_routes = [
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

routes = {}

for r in list_of_routes:
    current = routes
    segs = r.split('/')

    for seg in segs:
        if seg in current:
            current = current[seg]
        else:
            current[seg] = {}


def print_routes(rts, sep):
    for rt in rts:
        print(sep + rt)

        if type(rts[rt]) is dict:
            print_routes(rts[rt], ' ' + sep)


print_routes(routes, '-')
