import functools
from collections import namedtuple
from hashtable.hashtable import HashTable


# Cheesy built in method of solving the problem at hand
@functools.lru_cache(maxsize=None)
def expensive_seq_done(x, y, z):
    if x <= 0:
        return y + z
    if x > 0:
        return expensive_seq_done(x-1, y+1, z) + expensive_seq_done(x-2, y+2, z*2) + expensive_seq_done(x-3, y+3, z*3)


def hash_check(key: str, value=None):
    ht = HashTable(0x10000)
    if ht.get(key) is not None:
        return ht.get(key)
    else:
        return ht.put(key, value)


def expensive_seq(x: int, y: int, z: int) -> int:
    if x <= 0:
        return y + z
    if x > 0:
        h1 = hash_check(f'{x}-1, {y}+1, {z}', expensive_seq_done(x-1, y+1, z))
        h2 = hash_check(f'{x}-2, {y}+2, {z}*2', expensive_seq_done(x-2, y+2, z*2))
        h3 = hash_check(f'{x}-3, {y}+3, {z}*3', expensive_seq_done(x-3, y+3, z*3))
        return h1 + h2 + h3


if __name__ == "__main__":
    for i in range(50):
        num = expensive_seq(i * 2, i * 3, i * 4)
        print(f"{i * 2} {i * 3} {i * 4} = {num}")
    #
    # print(expensive_seq(2, 3, 4))
