import pytest
from members.paikabluu.w1.translate import primes_up_to


def test_invalid_and_low():
    assert primes_up_to(-10) == []
    assert primes_up_to(-1) == []
    assert primes_up_to(0) == []
    assert primes_up_to(1) == []


def test_smallest():
    assert primes_up_to(2) == [2]


def test_perfect_square_composites():
    assert primes_up_to(4) == [2, 3]
    assert primes_up_to(9) == [2, 3, 5, 7]
    assert 25 not in primes_up_to(25)


def test_standard_range():
    assert primes_up_to(10) == [2, 3, 5, 7]
    assert primes_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_large_input():
    result = primes_up_to(100)
    
    assert isinstance(result, list)
    assert len(result) == 25 
    assert all(isinstance(p, int) for p in result)
    assert result[-1] == 97  