from ..main import *    # noqa:F403


def test_custom_zip():
    params = (['A', 'B', 'C'], [1, 2, 3])
    expected = [('A', 1), ('B', 2), ('C', 3)]
    assert list(custom_zip(*params)) == expected    # noqa:F405
