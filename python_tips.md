### List

```
list.append # add to the end of list
list.extend # add another list to list updating list
list.insert(0, 'here') insert into specific index
del list[0] remove from list[0]
list.pop() remove from top of list
list.pop(0) remove item at index 0

list.copy() #shallow copy
len(list)

concat = list1 + list2
```

### Dict

```
dict['key']  # add to the dict
del dict['key'] #delete element at key, key must exist

dict.keys()
dict.values()
dict.items()

```

```
"hello, world".split()
"hello, world".join(',')

quote = "the greatest teacher failure is"

words = quote.split()
```

### classes

```
**kwargs = dict of keyword args
**args = list of args

setattr(self,key, value)

getattr(self, key)

super() # call __init__ of parent class

issubclass(subclass, class)
isinstance(class, parentClass)
__class__

magic methods
do this mostly on the base classes

__str__ #should return a user friendly representation of class
__init__
__repr__ #should return a programmer friendly representation of class
__call__


__new__

class ReversedStr(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self
```

#### Set

```
union |
intersection &

difference -
symmetric_difference ^

update
add
disgard
remove
```

#### Shallow vs Deep Copies

Shallow copy keep reference if other list, dict, tuple are in the list, dict, tuple (childred object)
Deep create a independent copy
