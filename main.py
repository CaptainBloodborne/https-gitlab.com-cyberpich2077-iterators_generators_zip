from typing import Sequence


def custom_zip(*args: Sequence):
    """
    Generator function equivalent to built-in
    function zip()
    ---------

    :param args: any number of Sequence objects
    :return: Generator object with tuples
    """
    for i in range(len(min(*args, key=len))):
        yield tuple([j[i] for j in args])


abc = custom_zip("ABC", ["a", "b", "c"], range(3))
print(list(abc))
