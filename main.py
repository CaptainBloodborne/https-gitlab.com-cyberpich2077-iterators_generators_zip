from typing import Sequence


def custom_zip(*args: Sequence):
    """
    Generator function
    ---------

    :param args: any number of Sequence objects
    :return: Generator object with tuples
    """
    if args:
        for i in range(len(min(*args, key=len))):
            yield tuple([j[i] for j in args])
