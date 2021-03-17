### Generators/Iterators module, zip task
***
#### Description

Create you own `zip` function with the same behaviour as build-in `zip` function and returns iterator.
Your function name should be `custom_zip`.

Don't use build-in `zip` function or `itertools`.

#### Example


    >>> list(custom_zip(['A', 'B', 'C'], [1, 2, 3]))
        [('A', 1), ('B', 2), ('C', 3)]
    
    >>> list(custom_zip('!', ['A', 'B', 'C', 'D'], range(1, 3)))
        [('!', 'A', 1)]
    
    >>> c = custom_zip('abcd', ['A', 'B', 'C', 'D'], range(0, 40)))
    >>> next(c)
        ('a', 'A', 0)
    >>> next(c)
        ('b', 'B', 1)
    ...
        