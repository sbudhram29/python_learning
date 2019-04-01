
from collections import namedtuple

Company = namedtuple("Company", "name id library email")


etcetera = Company('Etcetera', 2, 'etlib', 'etmail@carlisle-etcetera.com')
carlisle = Company('Carlisle', 1, 'acsdbase', 'ccmail@carlisle-etcetera.com')


print(etcetera)
print(carlisle)
