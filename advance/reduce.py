from operator import add
from functools import reduce

prices = [
    (6.99, 5),
    (2.94, 15),
    (156.99, 2),
    (99.99, 4),
    (1.82, 102)
]


def product_sales(product):
    return product[0] * product[1]


total = reduce(add, map(product_sales, prices))

print(total)

courses = {'count': 2,
           'title': 'Django Basics',
           'prereqs': [{'count': 3,
                        'title': 'Object-Oriented Python',
                        'prereqs': [{'count': 1,
                                     'title': 'Python Collections',
                                     'prereqs': [{'count': 0,
                                                  'title': 'Python Basics',
                                                  'prereqs': []}]},
                                    {'count': 0,
                                     'title': 'Python Basics',
                                     'prereqs': []},
                                    {'count': 0,
                                     'title': 'Setting Up a Local Python Environment',
                                     'prereqs': []}]},
                       {'count': 0,
                        'title': 'Flask Basics',
                        'prereqs': []}]}


def prereqs(data, pres=None):
    pres = pres or set()

    for prereq in data['prereqs']:
        pres.add(prereq['title'])
        if(len(prereq['prereqs'])):
            prereqs(prereq, pres)
    return pres


print(prereqs(courses, None))
