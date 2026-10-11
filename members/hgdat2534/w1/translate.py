def insertion_sort(a: list[int]) -> list[int]:
    """Sort a list in-place using insertion sort and return the sorted list.

    Difference from C++:
    In C++, sorting in-place requires passing the vector by reference
    (`std::vector<int>& a`), otherwise a copy is sorted. In Python, lists are
    mutable objects passed by object reference, so reassigning elements (`a[j + 1] = ...`)
    mutates the caller's list directly without reference syntax. Python also
    uses `range(1, len(a))` and `and` instead of a C-style `for` loop and `&&`.

    >>> nums = [5, 2, 4, 6, 1, 3]
    >>> insertion_sort(nums)
    [1, 2, 3, 4, 5, 6]
    >>> nums  # Modified in-place
    [1, 2, 3, 4, 5, 6]
    """

    for i in range (1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a