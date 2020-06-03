# colorUnsorted: list = [("aqua", "#00FFFF"), ("beige", "#F5F5DC"), ("chartreuse", "#7FFF00")];
# colorSorted: list = [("aqua", "#00FFFF"), ("chartreuse", "#7FFF00"), ("beige", "#F5F5DC")];

# 0(n)
# for color in colorUnsorted:
#     print(color)
# o(log n)
# if using a binary search
# requires a sorted list
# colorSorted.sort()
# print(colorSorted)

# The requirements for a hash function are:

# A hash function must be consistent (deterministic). Every time it receives the same input (like "aqua"), it must return the same output (like 4).
#  If it’s not deterministic, it is not a hash function.
# Different input data should return different numbers. For example, if the input "aqua" returns 4, then the input "beige" should not return 4.
# A hash function must return numbers that are within a specific range.

# What’s the point of a hashing function? How does a function that maps data to a number get us any closer to a data structure with constant lookup time?

# We can combine a hash function with an array to achieve this. Imagine that we know we have five colors to store in our data structure.
# We can start with a list that has five empty slots.

colors: list = [None] * 5

# Naive Implementation
# As we discussed above, hashing functions take an input (usually a string) and return an integer as the output. 
# To convert a string into an integer, hashing functions operate on the individual characters that make up the string.

def string_hashing(string: str, list_size: int) -> int:
    string_bytes = string.encode()
    sum: int = 0
    for byte in string_bytes:
        sum += byte
    return sum % list_size

# Setting value at reference to the index provided by hashing
colors[string_hashing("aqua", len(colors))] = "#00FFFF"
# Printing the element at the index provided by hashing
print(colors[string_hashing("aqua", len(colors))])
# The simple hash table we just created does not handle collisions (again, we cover more about collisions soon).
# It can search, insert, and delete all in constant time (O(1)).