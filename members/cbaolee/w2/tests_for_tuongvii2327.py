from members.tuongvii2327.w1.translate import is_valid_parentheses as valid


def test_empty_string_is_valid():
    assert valid("")

def test_sequential_pairs_are_valid():
    assert valid("()" * 6)

def test_extra_close_is_invalid():
    assert not valid("(" * 5 + ")" * 6)

def test_close_before_open_is_invalid():
    assert not valid(")(")

def test_unclosed_open_is_invalid():
    assert not valid("(" * 3)