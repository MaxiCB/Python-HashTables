import itertools
"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

q = set(range(1, 10))
# q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


def sum_diff(a, b, c, d):
    _a, _b, _c, _d = f(a), f(b), f(c), f(d)
    if _a + _b == _c - _d:
        print(f'f({a}) + f({b}) = f({c}) - f({d})  {_a} + {_b} = {_c} - {_d}')


if __name__ == '__main__':
    carts = list(itertools.product(q, repeat=4))
    for _set in carts:
        sum_diff(*_set)
