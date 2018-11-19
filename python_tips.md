### List

```
list.append # add to the end of list
list.extend # add another list to list updating list
list.insert(0, 'here') insert into specific index
del list[0] remove from list[0]
list.pop() remove from top of list
list.pop(0) remove item at index 0

list.copy()
len(list)

concat = list1 + list2
```

### strings

```
"".split()
"".join(',')

quote = "the greatest teacher failure is"

words = quote.split()
```

### classes

```
**kwargs = dict of keyword args
**args = list of args
setattr(self,key, value)
getattr(self, key)

super() to override __init__

issubclass(subclass, class)
isinstance(class, parentClass)
__class__

magic methods
do this mostly on the base classes

__str__ = return string of object
__int__
__init__
__repr__


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
