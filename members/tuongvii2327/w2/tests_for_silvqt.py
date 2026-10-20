import importlib


def _merge() -> None:
    m = importlib.import_module("members.SilvQT.w1.translate")
    return m.merge_sorted_arrays


def test_interleaved() -> None:
    assert _merge()([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_unequal_lengths() -> None:
    assert _merge()([1], [2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert _merge()([2, 3, 4, 5], [1]) == [1, 2, 3, 4, 5]


def test_one_side_empty() -> None:
    assert _merge()([], [1, 2]) == [1, 2]
    assert _merge()([1, 2], []) == [1, 2]


def test_both_empty() -> None:
    assert _merge()([], []) == []


def test_duplicates_kept() -> None:
    assert _merge()([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]


def test_negative_numbers() -> None:
    assert _merge()([-5, 0, 3], [-2, 4]) == [-5, -2, 0, 3, 4]


def test_inputs_not_modified() -> None:
    a, b = [1, 3], [2, 4]
    _merge()(a, b)
    assert a == [1, 3] and b == [2, 4]


def test_returns_new_list() -> None:
    a = [1, 2]
    result = _merge()(a, [])
    assert result == a and result is not a
