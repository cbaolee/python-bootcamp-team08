from members.hgdat2534.w1.translate import insertion_sort


def test_insertion_sort_normal():
    assert insertion_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]


def test_insertion_sort_already_sorted():
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_insertion_sort_reverse():
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_insertion_sort_duplicates():
    assert insertion_sort([7, 7, 3, 3, 7]) == [3, 3, 7, 7, 7]


def test_insertion_sort_edge_case_empty():
    assert insertion_sort([]) == []


def test_insertion_sort_edge_case_sinlge():
    assert insertion_sort([25]) == [25]
