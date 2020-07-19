def namelist(names):
    if not(len(names)):
        return ''
    if len(names) == 1:
        return names[0]['name']

    # loop through names and add to array

    arr = []
    for name in names:
        arr.append(name['name'])
    # create string with separated by comma
    last = arr.pop()

    begin = ', '.join(arr)

    return begin + ' & ' + last

    # add a & for the last name


# print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
# # returns 'Bart, Lisa & Maggie'

# print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
# # returns 'Bart & Lisa'

# print(namelist([{'name': 'Bart'}]))
# # returns 'Bart'
