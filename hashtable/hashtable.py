class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity: int = MIN_CAPACITY):
        self.arr: list[HashTableEntry] = [None] * capacity
        self.capacity: int = capacity
        self.size: int = 0
        self.load_factor = 0

    def get_num_slots(self) -> int:
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.arr)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        self.load_factor = self.size / self.capacity
        return self.load_factor

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass

    def djb2(self, key: str) -> int:
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hsh: int = 5381
        bytes: list[int] = key.encode('utf-8')
        # Building upon hsh while iterating through the string
        #
        for i in bytes:
            # Lock to 32bit to avoid overflows - 0x100000000
            # This could just as well be % self.size to ensure we are never out of bounds
            hsh = ((hsh * 33) ^ i) % 0x100000000
        return hsh

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key: str, value: str):
        """
        Store the value with the given key.

        Hash collisions should be handled withLinked List Chaining.

        Implement this.
        """

        if self.arr[self.hash_index(key)] is None:
            self.arr[self.hash_index(key)] = HashTableEntry(key, value)
            self.size += 1
        else:
            self.arr[self.hash_index(key)] = HashTableEntry(key, value)
        self.get_load_factor()
        if self.load_factor >= 0.75:
            self.rehash(True)
        return self.arr[self.hash_index(key)].value


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        self.arr[self.hash_index(key)] = None
        self.size = self.size - 1
        self.get_load_factor()
        if self.load_factor <= 0.2:
            self.rehash(False)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        if self.arr[self.hash_index(key)] is not None:
            return self.arr[self.hash_index(key)].value
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity // 2
        self.rehash(True)

    def rehash(self, up: bool):
        temp = self.arr
        if up:
            self.arr = [None] * (self.capacity * 2)
            self.capacity = self.capacity * 2
        if not up:
            self.arr = [None] * (self.capacity // 2)
            self.capacity = self.capacity // 2
        self.size = 0

        for item in temp:
            if item is not None:
                self.put(item.key, item.value)


if __name__ == "__main__":
    ht = HashTable(20)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

# Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

# Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

# Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
