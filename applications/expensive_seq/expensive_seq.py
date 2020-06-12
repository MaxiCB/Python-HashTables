import functools
from hashtable.hashtable import HashTable

hashed = HashTable()


@functools.lru_cache(maxsize=None)
def expensive_seq(x, y, z):
    t1 = (f'{x} - 1', f'{y} + 1', f'{z}')
    t2 = (f'{x} - 2', f'{y} + 2', f'{z}*2')
    t3 = (f'{x} - 3', f'{y} + 3', f'{z}*3')
    if x <= 0:
        return y + z
    if x > 0:
        # if hashed.get(''.join(t1)) is not None:
        #     first = hashed.get(''.join(t1))
        # else:
        #     first = hashed.put(''.join(t1), expensive_seq(x - 1, y + 1, z))
        # if hashed.get(''.join(t2)) is not None:
        #     second = hashed.get(''.join(t2))
        # else:
        #     second = hashed.put(''.join(t2), expensive_seq(x - 2, y + 2, z*2))
        # if hashed.get(''.join(t3)) is not None:
        #     third = hashed.get(''.join(t3))
        # else:
        #     third = hashed.put(''.join(t3), expensive_seq(x - 3, y + 3, z*3))
        #
        # return first + second + third
        return expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)


if __name__ == "__main__":
    for i in range(2):
        num = expensive_seq(i * 2, i * 3, i * 4)
        # print(f"{i * 2} {i * 3} {i * 4} = {num}")

    # print(expensive_seq(2, 3, 4))
