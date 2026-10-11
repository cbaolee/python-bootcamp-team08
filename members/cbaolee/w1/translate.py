"""
binary search on a sorted list
"""

def binary_search(a: list[int], key: int) -> int:
    """ list in Python and vector in C++ both are dynamic arrays, however vector just store one datatype, list can store many different data types """
    lo: int = 0
    hi: int = len(a) - 1

    while lo <= hi:
        mid: int = lo + int((hi - lo) / 2)

        if a[mid] == key:
            return mid
        elif a[mid] > key:
            hi = mid - 1
        else:
            lo = mid + 1

    return -1